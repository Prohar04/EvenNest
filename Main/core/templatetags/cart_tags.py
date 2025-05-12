from django import template
from django.db.models import Sum
from core.models import Cart

register = template.Library()

@register.simple_tag
def cart_item_count(user):
    """Returns the total number of items in the user's cart, including quantities"""
    if user.is_authenticated:
        cart = Cart.objects.filter(user=user).first()
        if cart:
            total = cart.items.aggregate(total=Sum('quantity'))['total']
            return total or 0
    return 0

@register.filter
def get_wishlist_status(item, user):
    """Check if an item is in user's wishlist"""
    if user.is_authenticated:
        return user.wishlist_set.filter(items=item).exists()
    return False