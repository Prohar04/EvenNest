# EventNest - Professional Event Management Platform

A modern, professional event management system built with Django, featuring a sleek black-themed interface with accent colors. EventNest enables users to discover, book, and manage professional event services and essentials.

## 🎨 Design Features

### Visual Design
- **Dark Theme**: Elegant black background (#0a0e27) with dark accents
- **Accent Color**: Indigo/Iris purple (#6366f1) for highlights and CTAs
- **Typography**: Modern, professional fonts with clear hierarchy
- **Responsive**: Mobile-first design that works perfectly on all devices
- **Smooth Interactions**: Hover effects, transitions, and animations

### Key Pages
1. **Home Page** - Hero section, service showcase, featured products, CTA sections
2. **Services Page** - Browse professional services by category
3. **Service Detail** - Complete service information with booking functionality
4. **Store** - Shop for event essentials with search and filters
5. **Cart & Checkout** - Complete shopping experience
6. **Authentication** - Modern login and registration forms
7. **User Dashboard** - Profile, orders, and bookings

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Django 5.2+
- pip package manager

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Prohar04/EventNest.git
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

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Load sample data (optional)**
   ```bash
   python manage.py loaddata fixtures/initial_products.json
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` to view the site.

## 📁 Project Structure

```
EventNest/Main/
├── core/                          # Main Django app
│   ├── templates/
│   │   ├── base_new.html          # Modern base template
│   │   ├── home_new.html          # Home page
│   │   ├── footer_new.html        # Footer component
│   │   ├── registration/
│   │   │   ├── login_new.html     # Login page
│   │   │   └── signup_new.html    # Signup page
│   │   ├── services/
│   │   │   ├── all_services_new.html
│   │   │   └── service_detail_new.html
│   │   └── store/
│   │       ├── all_items_new.html
│   │       ├── item_detail_new.html
│   │       └── cart_new.html
│   ├── static/css/
│   │   └── theme.css              # Main stylesheet with design system
│   ├── models.py                  # Database models
│   ├── views.py                   # View logic
│   ├── forms.py                   # Form definitions
│   ├── admin.py                   # Admin interface
│   └── urls.py                    # URL routing
├── media/                         # User uploads (images)
│   ├── services/                  # Service images
│   └── store/                     # Store item images
├── myproject/
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Main URL configuration
│   ├── wsgi.py                    # WSGI server config
│   └── wsgi_vercel.py            # Vercel deployment config
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── vercel.json                   # Vercel deployment config
├── .env.example                  # Environment variables template
└── README.md                     # This file
```

## 🗄️ Database Models

### Core Models
- **User** - Django auth user
- **UserProfile** - Extended user information
- **Service** - Professional services (events, photography, catering, printing)
- **ServiceCategory** - Service categories
- **StoreItem** - Retail items for events
- **StoreCategory** - Store item categories
- **Cart** - Shopping cart
- **Order** - Customer orders
- **Booking** - Service bookings
- **Wishlist** - User wishlists

## 🎯 Key Features

### For Users
- ✅ Browse services and store items
- ✅ Add items to cart and checkout
- ✅ Book professional services
- ✅ Manage wishlist
- ✅ View order and booking history
- ✅ User profile management

### For Admin
- ✅ Django admin interface
- ✅ Service management
- ✅ Product catalog management
- ✅ Order management
- ✅ User management
- ✅ Analytics dashboard

## 🌐 Deployment to Vercel

### Prerequisites
- Vercel account (https://vercel.com)
- GitHub repository with EventNest code
- MySQL database (using Aiven or another provider)

### Steps

1. **Prepare for deployment**
   ```bash
   # Collect static files
   python manage.py collectstatic --noinput --clear
   ```

2. **Configure environment variables**
   - In Vercel project settings, add:
     ```
     DJANGO_SECRET_KEY=your-secret-key
     DJANGO_DEBUG=False
     DATABASE_URL=mysql://user:password@host:port/dbname
     ALLOWED_HOSTS=yourvercelapp.vercel.app,yourdomain.com
     ```

3. **Push to GitHub**
   ```bash
   git add -A
   git commit -m "Ready for Vercel deployment"
   git push origin main
   ```

4. **Deploy on Vercel**
   - Go to https://vercel.com/new
   - Select your GitHub repository
   - Import project
   - Add environment variables
   - Click "Deploy"

5. **Database initialization**
   After first deployment, run migrations:
   ```bash
   vercel env pull  # Pull environment variables
   python manage.py migrate
   ```

## 🛠️ Environment Variables

Create a `.env` file in the project root:

```env
# Django
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True

# Database (Local - SQLite)
# Default: sqlite:///db.sqlite3

# Database (Production - MySQL)
DATABASE_URL=mysql://user:password@host:port/dbname

# Allowed Hosts
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Vercel
VERCEL_URL=your-vercel-app.vercel.app
CUSTOM_DOMAIN=yourdomain.com
```

## 📦 Dependencies

Key packages included:
- Django 5.2 - Web framework
- Channels - WebSocket support
- crispy-forms - Form rendering
- PyMySQL - MySQL database driver
- Whitenoise - Static file serving
- python-dotenv - Environment management

See `requirements.txt` for complete list.

## 🎨 Customization

### Colors
Edit CSS variables in `core/static/css/theme.css`:
```css
:root {
    --color-accent: #6366f1;        /* Change primary accent */
    --color-text: #f1f5f9;          /* Change text color */
    --color-black: #0a0e27;         /* Change background */
}
```

### Fonts
Update font imports in templates for custom typography.

### Services and Categories
Add services and categories through Django admin interface.

## 📊 Admin Interface

Access the admin panel at `/admin/` with superuser credentials to:
- Manage services and categories
- Manage store inventory
- View and process orders
- Manage user accounts
- View analytics

## 🔒 Security

- CSRF protection enabled
- SQL injection prevention
- XSS protection
- Environment variable security
- SSL/TLS ready for production

## 📱 Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🐛 Troubleshooting

### Database Connection Issues
```bash
# Test database connection
python manage.py dbshell
```

### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput --clear
```

### Permission Errors
```bash
# Check file permissions
chmod -R 755 media/
chmod -R 755 staticfiles/
```

## 📝 License

This project is private and owned by Prohar04. All rights reserved.

## 📧 Support

For issues and support, contact the development team or create an issue in the GitHub repository.

## 🚀 Future Enhancements

- [ ] Real-time chat between users and providers
- [ ] Advanced analytics dashboard
- [ ] Payment gateway integration
- [ ] Email notifications
- [ ] SMS notifications
- [ ] Mobile app
- [ ] API documentation
- [ ] Enhanced search with filters

---

Built with ❤️ by the EventNest Team
