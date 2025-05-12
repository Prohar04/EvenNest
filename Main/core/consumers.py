import json
import asyncio
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from django.conf import settings
from .models import Message, Chat, ChatSession

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    connected_users = {}  # In-memory tracking of connected users

    async def connect(self):
        try:
            self.chat_id = self.scope['url_route']['kwargs']['chat_id']
            self.room_group_name = f'chat_{self.chat_id}'
            self.user = self.scope['user']
            self.last_activity = None
            self.is_connected = False

            if not self.user.is_authenticated:
                logger.warning(f"Unauthenticated connection attempt to chat {self.chat_id}")
                await self.close(code=4001)
                return

            chat_exists = await self.chat_exists()
            if not chat_exists:
                logger.warning(f"User {self.user.username} attempted to access nonexistent chat {self.chat_id}")
                await self.close(code=4004)
                return

            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            # Track user presence
            ChatConsumer.connected_users[f"{self.room_group_name}_{self.user.username}"] = True
            self.is_connected = True  # Set connected state before accept
            await self.accept()
            
            self.last_activity = timezone.now()

            # Send connection confirmation
            await self.send_json({
                'type': 'connection_established',
                'message': 'Connected to chat'
            })

            logger.info(f"User {self.user.username} connected to chat {self.chat_id}")

        except Exception as e:
            logger.error(f"Connection error in chat {self.chat_id}: {str(e)}")
            if hasattr(self, 'is_connected') and self.is_connected:
                await self.close(code=4000)

    async def disconnect(self, close_code):
        try:
            if hasattr(self, 'room_group_name'):
                # Remove user from room group
                await self.channel_layer.group_discard(
                    self.room_group_name,
                    self.channel_name
                )
                # Remove user from connected users
                user_key = f"{self.room_group_name}_{self.user.username}"
                ChatConsumer.connected_users.pop(user_key, None)
                
                if hasattr(self, 'user'):
                    await self.update_user_status(False)

            self.is_connected = False
            logger.info(f"User {self.user.username} disconnected from chat {self.chat_id}")

        except Exception as e:
            logger.error(f"Disconnect error in chat {self.chat_id}: {str(e)}")

    async def receive(self, text_data):
        try:
            if not self.is_connected:
                await self.send_error('Not connected')
                return

            try:
                data = json.loads(text_data)
            except json.JSONDecodeError:
                await self.send_error('Invalid message format')
                return

            message_type = data.get('type', 'message')
            self.last_activity = timezone.now()

            if message_type == 'typing':
                await self.handle_typing_status(data)
            elif message_type == 'message':
                if not data.get('message', '').strip():
                    await self.send_error('Message cannot be empty')
                    return
                await self.handle_chat_message(data)
            else:
                await self.send_error(f'Unknown message type: {message_type}')

        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            await self.send_error('Failed to process message')

    async def handle_chat_message(self, data):
        try:
            message = data.get('message', '').strip()
            if not message:
                return

            # Check if user is still connected
            user_key = f"{self.room_group_name}_{self.user.username}"
            if not ChatConsumer.connected_users.get(user_key):
                await self.send_error('Connection lost')
                await self.close(code=4003)
                return

            # Save message to database
            try:
                db_message = await self.save_message(message)
            except Exception as e:
                logger.error(f"Error saving message: {str(e)}")
                await self.send_error('Failed to save message')
                return

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': self.user.username,
                    'timestamp': db_message.created_at.isoformat(),
                    'is_staff': self.user.is_staff
                }
            )
            
            # Send confirmation to sender
            await self.send_json({
                'type': 'message_sent',
                'message_id': db_message.id
            })

        except Exception as e:
            logger.error(f"Error handling chat message: {str(e)}")
            await self.send_error('Failed to send message')

    async def handle_typing_status(self, data):
        try:
            is_typing = data.get('is_typing', False)
            await self.update_user_status(is_typing)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'typing_status',
                    'user': self.user.username,
                    'is_typing': is_typing
                }
            )
        except Exception as e:
            logger.error(f"Error handling typing status: {str(e)}")
            await self.send_error('Failed to update typing status')

    async def chat_message(self, event):
        try:
            # Check if user is still connected
            user_key = f"{self.room_group_name}_{self.user.username}"
            if not ChatConsumer.connected_users.get(user_key):
                return
                
            await self.send_json({
                'type': 'message',
                'message': event['message'],
                'sender': event['sender'],
                'timestamp': event['timestamp'],
                'is_staff': event['is_staff']
            })
        except Exception as e:
            logger.error(f"Error sending chat message: {str(e)}")

    async def typing_status(self, event):
        try:
            # Check if user is still connected
            user_key = f"{self.room_group_name}_{self.user.username}"
            if not ChatConsumer.connected_users.get(user_key):
                return
                
            await self.send_json({
                'type': 'typing',
                'user': event['user'],
                'is_typing': event['is_typing']
            })
        except Exception as e:
            logger.error(f"Error sending typing status: {str(e)}")

    async def send_error(self, message):
        try:
            await self.send_json({
                'type': 'error',
                'message': message
            })
        except Exception as e:
            logger.error(f"Error sending error message: {str(e)}")

    async def send_json(self, content):
        try:
            if self.is_connected:
                await self.send(text_data=json.dumps(content))
        except Exception as e:
            logger.error(f"Error sending JSON: {str(e)}")

    @database_sync_to_async
    def save_message(self, content):
        chat = Chat.objects.get(id=self.chat_id)
        message = Message.objects.create(
            chat=chat,
            sender=self.user,
            content=content,
            is_read=self.user.is_staff
        )
        return message

    @database_sync_to_async
    def update_user_status(self, is_typing):
        chat = Chat.objects.get(id=self.chat_id)
        chat.update_user_status(self.user, is_typing)

    @database_sync_to_async
    def chat_exists(self):
        try:
            chat = Chat.objects.get(id=self.chat_id)
            return self.user.is_staff or chat.user == self.user
        except Chat.DoesNotExist:
            return False