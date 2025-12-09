"""
EventNest - Main Views
Production-ready views for all core functionality
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.db.models import Q, Prefetch, Sum
from django.views.decorators.http import require_POST
from django.views.decorators.cache import cache_page
from django.db import transaction
from functools import wraps
from .forms import SignUpForm, BookingForm
from .models import (
    ServiceCategory, Service, StoreCategory, StoreItem, 
    Cart, CartItem, Order, OrderItem, Wishlist,
    UserProfile, Booking, Contact
)
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


def login_required_view(view_func):
    """Custom decorator to require login for specific views"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f'/login/?next={request.path}')
        return view_func(request, *args, **kwargs)
    return wrapper


# ============== HOME & LANDING ==============

def home(request):
    """Home/Landing page"""
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Get featured items (latest 8)
    featured_items = StoreItem.objects.all()[:8]
    
    context = {
        'featured_items': featured_items,
        'services': Service.objects.all()[:3],
    }
    return render(request, 'home.html', context)


# ============== AUTHENTICATION ==============

def signup_view(request):
    """User registration"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['full_name'].split()[0]
            user.save()
            
            # Create user profile
            UserProfile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name']
            )
            
            # Create cart
            Cart.objects.create(user=user)
            
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    
    context = {}
    return render(request, 'registration/login.html', context)


def logout_view(request):
    """User logout"""
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('home')
    else:
        # Redirect to home if someone tries to access logout via GET
        return redirect('home')


# ============== USER PROFILE ==============

@login_required(login_url='login')
def profile(request):
    """User profile"""
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.save()
        
        profile = user.profile
        profile.phone = request.POST.get('phone', '')
        profile.address = request.POST.get('address', '')
        profile.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    
    return render(request, 'core/profile.html')


# ============== SERVICES ==============

@login_required(login_url='login')
def all_services(request):
    """Browse all services"""
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    
    services = Service.objects.all()
    
    if query:
        services = services.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        )
    
    if category_id:
        services = services.filter(category_id=category_id)
    
    categories = ServiceCategory.objects.all()
    
    context = {
        'services': services,
        'categories': categories,
        'query': query,
    }
    return render(request, 'services/all_services.html', context)


@login_required(login_url='login')
def service_detail(request, service_id):
    """Service detail page"""
    service = get_object_or_404(Service, id=service_id)
    
    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)


# ============== SERVICES - BOOKING ==============

@login_required(login_url='login')
def request_service_quote(request, service_id):
    """Request a quote for a service"""
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        # Create contact inquiry
        contact = Contact.objects.create(
            user=request.user,
            full_name=request.user.first_name,
            email=request.user.email,
            subject=f"Quote Request - {service.title}",
            message=request.POST.get('message', ''),
            service_type='service',
            service_id=service.id,
            service_name=service.title
        )
        messages.success(request, 'Quote request sent! We will contact you soon.')
        return redirect('all_services')
    
    return render(request, 'services/service_detail.html', {'service': service})


@login_required(login_url='login')
def my_bookings(request):
    """View user's bookings"""
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'bookings': bookings,
    }
    return render(request, 'core/my_bookings.html', context)


# ============== STORE ==============

@login_required(login_url='login')
def all_store_items(request):
    """Browse all store items"""
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    
    items = StoreItem.objects.all()
    
    if query:
        items = items.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
    
    if category_id:
        items = items.filter(category_id=category_id)
    
    categories = StoreCategory.objects.all()
    
    context = {
        'items': items,
        'categories': categories,
        'query': query,
    }
    return render(request, 'store/all_items.html', context)


@login_required(login_url='login')
def store_item_detail(request, item_id):
    """Store item detail page"""
    item = get_object_or_404(StoreItem, id=item_id)
    
    context = {
        'item': item,
    }
    return render(request, 'store/item_detail.html', context)


# ============== SHOPPING CART ==============

@login_required(login_url='login')
def cart(request):
    """View shopping cart"""
    if not request.user.is_authenticated:
        return redirect('login')
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all().select_related('item')
    total = sum(item.get_total() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'store/cart.html', context)


@login_required(login_url='login')
@require_POST
def add_to_cart(request, item_id):
    """Add item to cart"""
    item = get_object_or_404(StoreItem, id=item_id)
    quantity = int(request.POST.get('quantity', 1))
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        item=item,
        defaults={'quantity': quantity}
    )
    
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    messages.success(request, f'{item.name} added to cart!')
    return redirect('cart')


@login_required(login_url='login')
@require_POST
def update_cart(request, cart_item_id):
    """Update cart item quantity"""
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    
    if cart_item.cart.user != request.user:
        raise Http404()
    
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart_item.quantity = min(quantity, cart_item.item.stock)
        cart_item.save()
    
    return redirect('cart')


@login_required(login_url='login')
def remove_from_cart(request, cart_item_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    
    if cart_item.cart.user != request.user:
        raise Http404()
    
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('cart')


# ============== CHECKOUT ==============

@login_required(login_url='login')
def checkout(request):
    """Checkout page"""
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all().select_related('item')
    total = sum(item.get_total() for item in cart_items)
    
    if not cart_items:
        return redirect('cart')
    
    if request.method == 'POST':
        # Create order
        order = Order.objects.create(
            user=request.user,
            total_amount=total,
            status='pending',
            shipping_address=f"{request.POST.get('address', '')}, {request.POST.get('city', '')}, {request.POST.get('zip_code', '')}"
        )
        
        # Create order items
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                item=cart_item.item,
                quantity=cart_item.quantity,
                price=cart_item.item.price
            )
        
        # Clear cart
        cart_items.delete()
        
        messages.success(request, 'Order placed successfully! Thank you for your purchase.')
        return redirect('order_history')
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'store/checkout.html', context)


# ============== ORDER HISTORY ==============

@login_required(login_url='login')
def order_history(request):
    """View order history"""
    orders = Order.objects.filter(user=request.user).prefetch_related('order_items__item').order_by('-created_at')
    
    context = {
        'orders': orders,
    }
    return render(request, 'store/order_history.html', context)


# ============== CONTACT ==============

@login_required(login_url='login')
def contact(request):
    """Contact form"""
    if request.method == 'POST':
        contact = Contact.objects.create(
            full_name=request.POST.get('full_name', ''),
            email=request.POST.get('email', ''),
            subject=request.POST.get('subject', ''),
            message=request.POST.get('message', ''),
            preferred_contact_method=request.POST.get('contact_method', 'email'),
            user=request.user if request.user.is_authenticated else None
        )
        messages.success(request, 'Your message has been sent! We will contact you soon.')
        return redirect('home')
    
    return render(request, 'core/contact.html')


# ============== API ENDPOINTS (JSON) ==============

@login_required(login_url='login')
def api_cart_count(request):
    """Get cart item count via AJAX"""
    try:
        cart = Cart.objects.get(user=request.user)
        count = cart.items.aggregate(total=Sum('quantity'))['total'] or 0
        return JsonResponse({'count': count})
    except Cart.DoesNotExist:
        return JsonResponse({'count': 0})


def api_services_search(request):
    """Search services via AJAX"""
    query = request.GET.get('q', '')
    services = Service.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )[:10].values('id', 'title', 'price')
    
    return JsonResponse(list(services), safe=False)


def api_items_search(request):
    """Search store items via AJAX"""
    query = request.GET.get('q', '')
    items = StoreItem.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )[:10].values('id', 'name', 'price')
    
    return JsonResponse(list(items), safe=False)


# ============== ERROR HANDLERS ==============

def handler404(request, exception):
    """404 error handler"""
    return render(request, '404.html', status=404)


def handler500(request):
    """500 error handler"""
    return render(request, '500.html', status=500)
