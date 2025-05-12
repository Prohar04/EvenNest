from django import template
from django.db.models import Q
from core.models import Message

register = template.Library()

@register.simple_tag
def unread_messages_count(user, chat=None):
    """Return the number of unread messages for a user
    If chat is provided, count only for that chat.
    Otherwise, count all unread messages."""
    if not user.is_authenticated:
        return 0
        
    messages = Message.objects.filter(is_read=False).exclude(sender=user)
    
    if chat:
        # Count unread messages for specific chat
        return messages.filter(chat=chat).count()
    elif user.is_staff:
        # For staff, count all unread messages across all chats
        return messages.count()
    else:
        # For regular users, count unread messages in their chats
        return messages.filter(chat__user=user).count()