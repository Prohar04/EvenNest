# EventNest - Production-Ready Event Management Platform

> **A modern, scalable, and feature-rich event management platform built with Django and modern web technologies.**

## Overview

EventNest is a complete event management solution that combines event discovery, professional services marketplace, and an integrated e-commerce store. It provides a seamless experience for users to browse events, book services, and purchase event merchandise.

### Key Features

✨ **Event Management**
- Browse and discover events
- Event categorization and search
- Event details with booking capabilities
- User dashboard for event management

🎯 **Services Marketplace**
- Professional event services (planning, photography, catering, etc.)
- Service details and pricing
- Service request/quote system
- Booking management

🛍️ **Online Store**
- Product catalog with categorization
- Shopping cart functionality
- Secure checkout process
- Order history and management
- Inventory tracking

👤 **User System**
- Secure authentication
- User profiles with preferences
- Booking history
- Order management
- Wishlist functionality

🔧 **Admin Dashboard**
- Complete content management
- Order and booking management
- User management
- Analytics and reporting
- Contact inquiry management

## Tech Stack

### Backend
- **Framework**: Django 5.2rc1
- **Database**: SQLite (dev) / MySQL (production)
- **ORM**: Django ORM
- **Task Queue**: Optional Celery support
- **Real-time**: Django Channels (setup ready)

### Frontend
- **HTML5** with Django Templates
- **CSS3** with custom design system
- **JavaScript** (vanilla, ES6+)
- **Bootstrap Icons** for beautiful iconography
- **Responsive Design** - Mobile-first approach

### Deployment
- **Hosting**: Vercel, Heroku, Railway, or traditional VPS
- **Static Files**: WhiteNoise for production
- **Database**: PostgreSQL (recommended for production)

## Project Structure

```
EventNest/
├── Main/
│   ├── core/                    # Main Django app
│   │   ├── models.py           # Database models
│   │   ├── views.py            # View functions
│   │   ├── forms.py            # Forms
│   │   ├── admin.py            # Admin configuration
│   │   ├── templates/          # HTML templates
│   │   │   ├── base.html       # Base template
│   │   │   ├── home.html       # Home page
│   │   │   ├── services/       # Service templates
│   │   │   ├── store/          # Store templates
│   │   │   ├── registration/   # Auth templates
│   │   │   └── core/           # User templates
│   │   ├── static/css/         # Stylesheets
│   │   ├── migrations/         # Database migrations
│   │   └── management/         # Management commands
│   ├── myproject/              # Project configuration
│   │   ├── settings.py         # Django settings
│   │   ├── urls.py             # URL routing
│   │   ├── wsgi.py             # WSGI config
│   │   └── asgi.py             # ASGI config
│   ├── media/                  # User uploads
│   ├── manage.py               # Django management script
│   └── requirements.txt         # Python dependencies
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Virtual environment (recommended)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/EventNest.git
   cd EventNest/Main
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data (optional)**
   ```bash
   python manage.py loaddata initial_products.json
   ```

8. **Start development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://localhost:8000`

## Database Models

### User & Profile
- **User** (Django built-in)
- **UserProfile** - Extended user information

### Services
- **ServiceCategory** - Service categories
- **Service** - Generic service model
- **EventManagement** - Event planning services
- **Photography** - Photography services
- **Catering** - Catering services
- **PrintingService** - Printing services
- **Booking** - Service bookings
- **Contact** - Contact inquiries

### Store
- **StoreCategory** - Product categories
- **StoreItem** - Products
- **Cart** - Shopping carts
- **CartItem** - Cart items
- **Order** - Orders
- **OrderItem** - Order items
- **Wishlist** - User wishlists

## API Endpoints

### Authentication
```
POST /login/                    - User login
POST /signup/                   - User registration
GET  /logout/                   - User logout
```

### Services
```
GET  /services/                 - List all services
GET  /services/<id>/            - Service details
POST /services/<id>/quote/      - Request service quote
GET  /my-bookings/              - User's bookings
```

### Store
```
GET  /store/                    - List all products
GET  /store/<id>/               - Product details
POST /cart/add/<id>/            - Add to cart
POST /cart/remove/<id>/         - Remove from cart
POST /cart/update/<id>/         - Update cart
GET  /cart/                     - View cart
POST /checkout/                 - Process checkout
GET  /orders/                   - Order history
```

### User
```
GET  /profile/                  - User profile
POST /profile/                  - Update profile
GET  /my-bookings/              - Bookings
```

### AJAX API
```
GET  /api/cart-count/           - Cart item count (JSON)
GET  /api/services-search/      - Search services (JSON)
GET  /api/items-search/         - Search items (JSON)
```

## Templates

### Core Templates
- `base.html` - Master template with navbar and footer
- `home.html` - Landing page
- `404.html` - 404 error page
- `500.html` - 500 error page

### Service Templates
- `services/all_services.html` - Services listing
- `services/service_detail.html` - Service details

### Store Templates
- `store/all_items.html` - Products listing
- `store/item_detail.html` - Product details
- `store/cart.html` - Shopping cart
- `store/checkout.html` - Checkout page
- `store/order_history.html` - Order history

### User Templates
- `registration/login.html` - Login page
- `registration/signup.html` - Registration page
- `core/profile.html` - User profile
- `core/my_bookings.html` - User bookings
- `core/contact.html` - Contact form

## Styling System

### Design Philosophy
- **Dark Theme** with purple accent (#6366f1)
- **Modern** and **Professional** aesthetic
- **Responsive** design for all devices
- **Accessible** color contrasts and interactions

### CSS Variables
```css
--primary: #6366f1           /* Main brand color */
--bg-primary: #0f172a        /* Dark background */
--text-primary: #f1f5f9      /* Light text */
--accent-blue: #0ea5e9
--accent-teal: #14b8a6
--accent-pink: #ec4899
--success: #10b981
--warning: #f59e0b
--error: #ef4444
```

### Component Classes
- `.btn` - Buttons
- `.card` - Cards
- `.grid` - Grid layout
- `.flex` - Flex layout
- `.badge` - Badges
- `.alert` - Alerts
- `.hero` - Hero section
- `.section` - Content sections

## Forms & Validation

All forms include:
- CSRF protection
- Input validation
- Error messages
- User-friendly feedback

## Security Features

✅ CSRF Protection
✅ SQL Injection Prevention (Django ORM)
✅ XSS Prevention (Template escaping)
✅ Secure Password Hashing
✅ Login Required Decorators
✅ User Permissions Management
✅ Secret Key in Environment Variables

## Performance Optimizations

- Database query optimization with `select_related()` and `prefetch_related()`
- Template caching
- Static file compression
- Lazy loading for images
- Minimal JavaScript bundle

## Deployment Guide

See `DEPLOYMENT_GUIDE.md` for detailed deployment instructions for:
- Vercel
- Heroku
- Railway
- Traditional VPS

## Admin Interface

Access admin at `/admin/` with superuser credentials.

**Admin Features:**
- Complete CRUD for all models
- User management
- Order management
- Service/Product management
- Contact inquiry management
- Booking management
- Custom actions and filters

## Future Enhancements

🔮 **Planned Features**
- Payment gateway integration (Stripe, PayPal)
- Email notifications
- SMS notifications
- Advanced analytics
- Review & rating system
- Event creation for users
- Social media integration
- Chat system for bookings
- Advanced search & filtering
- Multi-language support
- Mobile app (React Native)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For support, email support@eventnest.com or open an issue on GitHub.

## Authors

- **Lead Developer** - EventNest Team

## Changelog

### Version 1.0.0 (Current)
- ✅ Complete platform launch
- ✅ Services marketplace
- ✅ Online store
- ✅ User authentication
- ✅ Booking system
- ✅ Admin dashboard
- ✅ Modern UI/UX

---

**Built with ❤️ by EventNest Team**

For more information, visit: https://eventnest.com
