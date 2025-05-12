"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.personal_info, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),  # This includes additional auth URLs
    path('services/', views.all_services_view, name='all_services'),  # New URL for all services
    path('services/<str:category_name>/', views.service_category_view, name='service_category'),
    path('services/detail/<int:service_id>/', views.service_detail_view, name='service_detail'),  # New URL for service detail
    path('store/', views.all_store_items_view, name='all_store_items'),  # New URL for all store items
    path('store/<str:category_name>/', views.store_category_view, name='store_category'),
    path('store/detail/<int:item_id>/', views.store_item_detail_view, name='store_item_detail'),  # New URL for store item detail
    path('personal-info/', views.personal_info, name='personal_info'),
    path('search/', views.search, name='search'),  # Add search URL

    # Cart URLs
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),

    # Wishlist URLs
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:item_id>/', views.add_to_wishlist, name='add_to_wishlist'),

    # Chat URLs
    path('chat/', views.chat_list, name='chat_list'),
    path('chat/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('chat/start/', views.start_chat, name='start_chat'),
    path('chat/<int:chat_id>/message/', views.create_message, name='create_message'),
    path('chat/<int:chat_id>/messages/<int:last_message_id>/', views.get_new_messages, name='get_new_messages'),
    path('chat/<int:chat_id>/toggle_status/', views.toggle_chat_status, name='toggle_chat_status'),
    path('chat/<int:chat_id>/typing/', views.set_typing_status, name='set_typing_status'),
    path('chat/<int:chat_id>/typing/status/', views.get_typing_status, name='get_typing_status'),

    # Booking URLs
    path('bookings/', views.booking_list, name='booking_list'),
    path('book/<str:service_type>/<int:service_id>/', views.create_booking, name='create_booking'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
