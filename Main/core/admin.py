from django.contrib import admin
from .models import ServiceCategory, Service, StoreCategory, StoreItem, UserProfile, Cart, CartItem, Order, OrderItem, Wishlist, Booking
from .forms import ServiceForm, ServiceCategoryForm, StoreItemForm, StoreCategoryForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Add new service categories if they don't exist
def create_default_categories():
    ServiceCategory.objects.get_or_create(
        name='Caterer',
        defaults={'description': 'Professional catering services for events'}
    )
    ServiceCategory.objects.get_or_create(
        name='Card Designer',
        defaults={'description': 'Custom card design services for all occasions'}
    )

# Add new store categories if they don't exist
def create_default_store_categories():
    StoreCategory.objects.get_or_create(
        name='Decor Items',
        defaults={'description': 'Beautiful decorative items for all occasions'}
    )
    StoreCategory.objects.get_or_create(
        name='Event Accessories',
        defaults={'description': 'Essential accessories for event planning and decoration'}
    )

class ServiceInline(admin.TabularInline):
    model = Service
    form = ServiceForm
    extra = 1

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    form = ServiceCategoryForm
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [ServiceInline]

    def get_form(self, request, obj=None, **kwargs):
        if not ServiceCategory.objects.exists():
            create_default_categories()
        return super().get_form(request, obj, **kwargs)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceForm
    list_display = ('title', 'category', 'price', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 20

class StoreItemInline(admin.TabularInline):
    model = StoreItem
    form = StoreItemForm
    extra = 1

@admin.register(StoreCategory)
class StoreCategoryAdmin(admin.ModelAdmin):
    form = StoreCategoryForm
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [StoreItemInline]

    def get_form(self, request, obj=None, **kwargs):
        if not StoreCategory.objects.exists():
            create_default_store_categories()
        return super().get_form(request, obj, **kwargs)

@admin.register(StoreItem)
class StoreItemAdmin(admin.ModelAdmin):
    form = StoreItemForm
    list_display = ('name', 'category', 'price', 'stock', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone', 'created_at')
    search_fields = ('user__username', 'full_name', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('created_at',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'item', 'quantity', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('cart__user__username', 'item__name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'shipping_address')
    readonly_fields = ('total_amount',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'quantity', 'price')
    search_fields = ('order__user__username', 'item__name')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_count', 'created_at')
    search_fields = ('user__username',)
    filter_horizontal = ('items',)

    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = 'Number of Items'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'date', 'time_slot', 'status', 'total_amount', 'created_at')
    list_filter = ('service_type', 'status', 'date', 'created_at')
    search_fields = ('user__username', 'requirements', 'service_id')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
