from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)  # Format: +880XXXXXXXXXX
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create or update user profile"""
    # Skip profile creation here since it's handled in SignUpForm
    pass

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Service Categories"
        indexes = [
            models.Index(fields=['name']),
        ]

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category.name} - {self.title}"

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['price']),
        ]

class EventManagement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/events/')
    event_type = models.CharField(max_length=100)  # wedding, corporate, birthday, etc.
    capacity = models.IntegerField(help_text="Maximum number of guests")
    duration = models.IntegerField(help_text="Duration in hours")
    includes_decoration = models.BooleanField(default=False)
    includes_catering = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Event: {self.title}"

    def get_service_type(self):
        return 'event'

class Photography(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/photography/')
    shoot_type = models.CharField(max_length=100)  # wedding, portrait, event, etc.
    duration = models.IntegerField(help_text="Duration in hours")
    includes_editing = models.BooleanField(default=True)
    number_of_photos = models.IntegerField(help_text="Minimum number of delivered photos")
    includes_prints = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Photography: {self.title}"

    def get_service_type(self):
        return 'photo'

class Catering(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per person")
    image = models.ImageField(upload_to='services/catering/')
    cuisine_type = models.CharField(max_length=100)  # Bengali, Chinese, Continental, etc.
    min_order_quantity = models.IntegerField(help_text="Minimum number of persons")
    includes_serving_staff = models.BooleanField(default=False)
    includes_setup = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Catering: {self.title}"

    def get_service_type(self):
        return 'catering'

class PrintingService(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per piece")
    image = models.ImageField(upload_to='services/printing/')
    print_type = models.CharField(max_length=100)  # invitation, business card, banner, etc.
    paper_type = models.CharField(max_length=100)
    min_order_quantity = models.IntegerField()
    includes_design = models.BooleanField(default=False)
    delivery_time = models.IntegerField(help_text="Delivery time in days")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Printing: {self.title}"

    def get_service_type(self):
        return 'printing'

class StoreCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Store Categories"
        indexes = [
            models.Index(fields=['name']),
        ]

class StoreItem(models.Model):
    category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='store/')
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
        ]

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total(self):
        return sum(item.get_total() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure quantity doesn't exceed stock
        if self.quantity > self.item.stock:
            self.quantity = self.item.stock
        super().save(*args, **kwargs)

    def get_total(self):
        return self.item.price * self.quantity

@receiver(pre_save, sender=CartItem)
def cart_item_pre_save(sender, instance, **kwargs):
    """Ensure cart item quantity doesn't exceed available stock and update stock"""
    try:
        if instance.pk:  # If updating existing item
            old_item = CartItem.objects.get(pk=instance.pk)
            old_quantity = old_item.quantity
            quantity_diff = instance.quantity - old_quantity
            
            if quantity_diff > 0 and quantity_diff > instance.item.stock:
                instance.quantity = old_quantity + instance.item.stock
            
            # Update stock
            instance.item.stock = max(0, instance.item.stock - quantity_diff)
            instance.item.save()
        else:  # If creating new item
            if instance.quantity > instance.item.stock:
                instance.quantity = instance.item.stock
            
            # Update stock
            instance.item.stock = max(0, instance.item.stock - instance.quantity)
            instance.item.save()
    except CartItem.DoesNotExist:
        pass

@receiver(post_delete, sender=CartItem)
def cart_item_post_delete(sender, instance, **kwargs):
    """Return stock when cart item is deleted"""
    instance.item.stock += instance.quantity
    instance.item.save()

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(StoreItem, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    shipping_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new and self.status == 'cancelled':
            # Return stock for cancelled orders
            for order_item in self.order_items.all():
                order_item.item.stock += order_item.quantity
                order_item.item.save()

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at time of purchase
    
    def save(self, *args, **kwargs):
        if self.pk is None:  # Only for new items
            # Update stock when order item is created
            self.item.stock = max(0, self.item.stock - self.quantity)
            self.item.save()
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # Return stock when order item is deleted
        self.item.stock += self.quantity
        self.item.save()
        super().delete(*args, **kwargs)
    
    def get_total(self):
        return self.price * self.quantity

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(StoreItem, related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    last_message_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-last_message_at']
        indexes = [
            models.Index(fields=['-last_message_at']),
            models.Index(fields=['user', '-last_message_at']),
        ]

    def get_last_message(self):
        return self.messages.select_related('sender').first()
        
    def get_unread_count(self, user):
        return self.messages.filter(is_read=False).exclude(sender=user).count()
        
    def mark_messages_read(self, user):
        self.messages.filter(is_read=False).exclude(sender=user).update(is_read=True)
        
    def get_typing_users(self, exclude_user=None):
        """Get list of users currently typing in this chat"""
        typing_sessions = self.sessions.filter(
            is_typing=True,
            last_seen__gte=timezone.now() - timezone.timedelta(seconds=30)
        )
        if exclude_user:
            typing_sessions = typing_sessions.exclude(user=exclude_user)
        return [session.user for session in typing_sessions.select_related('user')]
        
    def update_user_status(self, user, is_typing=False):
        """Update user's typing status and last seen time"""
        session, _ = self.sessions.get_or_create(user=user)
        session.is_typing = is_typing
        session.save()

    def get_active_users(self):
        """Get list of users active in the last 5 minutes"""
        five_min_ago = timezone.now() - timezone.timedelta(minutes=5)
        sessions = self.sessions.filter(
            last_seen__gte=five_min_ago
        ).select_related('user')
        return [session.user for session in sessions]

    def get_user_presence(self, user):
        """Get presence info for a specific user"""
        session = self.sessions.filter(user=user).first()
        if not session:
            return {'online': False, 'last_seen': None}
            
        five_min_ago = timezone.now() - timezone.timedelta(minutes=5)
        return {
            'online': session.last_seen >= five_min_ago,
            'last_seen': session.last_seen
        }
        
    def __str__(self):
        return f"Chat with {self.user.username}"

class ChatSession(models.Model):
    """Track user sessions and typing status for chat"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_sessions')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='sessions')
    is_typing = models.BooleanField(default=False)
    last_seen = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['user', 'chat']
        indexes = [
            models.Index(fields=['user', 'chat']),
            models.Index(fields=['last_seen']),
        ]
    
    def __str__(self):
        return f"{self.user.username}'s session in chat {self.chat.id}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['chat', 'created_at']),
            models.Index(fields=['is_read']),
        ]
        
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new:
            # Update chat's last_message_at timestamp
            self.chat.last_message_at = self.created_at
            self.chat.save(update_fields=['last_message_at'])
    
    def __str__(self):
        return f"Message from {self.sender.username}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    SERVICE_CHOICES = [
        ('event', 'Event Management'),
        ('photo', 'Photography'),
        ('catering', 'Catering'),
        ('printing', 'Printing Service'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    service_id = models.PositiveIntegerField()
    date = models.DateField()
    time_slot = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requirements = models.TextField(blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['service_type', 'service_id']),
            models.Index(fields=['user', '-created_at']),
        ]
    
    def __str__(self):
        return f"{self.get_service_type_display()} booking by {self.user.username}"

    def get_service(self):
        if self.service_type == 'event':
            return EventManagement.objects.get(id=self.service_id)
        elif self.service_type == 'photo':
            return Photography.objects.get(id=self.service_id)
        elif self.service_type == 'catering':
            return Catering.objects.get(id=self.service_id)
        elif self.service_type == 'printing':
            return PrintingService.objects.get(id=self.service_id)
        return None
