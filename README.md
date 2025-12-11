# EventNest - Event Management Platform

![EventNest Logo](https://img.shields.io/badge/Event-Nest-blue?style=for-the-badge&labelColor=3B82F6&color=10B981)

A comprehensive event management platform built with Django, designed for the Bangladesh market. EventNest connects users with professional event services including photography, catering, event management, and printing services.

## 🌟 Features

### 🎯 Core Features
- **Service Booking System** - Book professional event services with date/time selection
- **E-commerce Store** - Purchase event-related products with cart & checkout
- **Wishlist** - Save favorite products for later
- **User Profiles** - Manage personal information and preferences
- **Notifications** - Real-time updates on bookings and orders
- **Search** - Find services and products quickly

### 📋 Service Categories
- 📸 **Photography** - Wedding, corporate, portrait photography
- 🍽️ **Catering** - Full-service catering for all events
- 🎉 **Event Management** - Complete event planning & coordination
- 🖨️ **Printing Services** - Invitations, banners, promotional materials

### 🛒 Store Features
- Product catalog with categories
- Shopping cart with quantity management
- Wishlist functionality
- Order history tracking
- Secure checkout process

### 👤 User Features
- User registration with phone validation (+880 format)
- Profile management
- Booking management (view, modify, cancel)
- Order tracking
- Notification center

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.13 | Backend language |
| Django | 5.2rc1 | Web framework |
| SQLite | 3 | Database |
| HTML/CSS | 5/3 | Frontend |
| Bootstrap Icons | 1.11 | Icons |
| JavaScript | ES6 | Interactivity |

## 📁 Project Structure

```
EventNest/
├── Main/
│   ├── core/                    # Main application
│   │   ├── models.py            # Database models
│   │   ├── views.py             # View functions
│   │   ├── forms.py             # Django forms
│   │   ├── context_processors.py # Template context
│   │   ├── templates/           # HTML templates
│   │   │   ├── base.html        # Base template
│   │   │   ├── home.html        # Homepage
│   │   │   ├── core/            # Core templates
│   │   │   ├── services/        # Service templates
│   │   │   ├── store/           # Store templates
│   │   │   └── registration/    # Auth templates
│   │   └── static/
│   │       ├── css/theme.css    # Custom styles
│   │       └── images/          # Static images
│   ├── media/                   # User uploads
│   ├── myproject/               # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── staticfiles/             # Collected static files
│   ├── manage.py
│   └── requirements.txt
└── README.md
```

## 🚀 Installation

### Prerequisites
- Python 3.10+
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Prohar04/EventNest.git
   cd EventNest
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   cd Main
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate sample data (optional)**
   ```bash
   python populate_data.py
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📊 Database Models

### Core Models
| Model | Description |
|-------|-------------|
| `User` | Django built-in user model |
| `UserProfile` | Extended user information (phone, address) |
| `Service` | Base service model |
| `ServiceCategory` | Service categories |
| `Photography` | Photography service details |
| `Catering` | Catering service details |
| `EventManagement` | Event management details |
| `PrintingService` | Printing service details |

### E-commerce Models
| Model | Description |
|-------|-------------|
| `StoreItem` | Products in the store |
| `StoreCategory` | Product categories |
| `Cart` | User shopping cart |
| `CartItem` | Items in cart |
| `Order` | Completed orders |
| `OrderItem` | Items in order |
| `Wishlist` | User wishlist |

### Booking & Notifications
| Model | Description |
|-------|-------------|
| `Booking` | Service bookings |
| `Notification` | User notifications |
| `Contact` | Contact form submissions |

## 🔗 URL Endpoints

### Public Pages
| URL | Description |
|-----|-------------|
| `/` | Homepage |
| `/services/` | All services |
| `/services/<id>/` | Service detail |
| `/store/` | Product store |
| `/store/item/<id>/` | Product detail |
| `/search/` | Search results |
| `/contact/` | Contact form |

### Authentication
| URL | Description |
|-----|-------------|
| `/login/` | User login |
| `/signup/` | User registration |
| `/logout/` | User logout |

### User Dashboard
| URL | Description |
|-----|-------------|
| `/profile/` | User profile |
| `/my-bookings/` | User bookings |
| `/order-history/` | Order history |
| `/wishlist/` | User wishlist |
| `/cart/` | Shopping cart |
| `/checkout/` | Checkout page |
| `/notifications/` | Notifications |

### Booking Actions
| URL | Description |
|-----|-------------|
| `/book/<service_id>/` | Book a service |
| `/booking/modify/<id>/` | Modify booking |
| `/booking/cancel/<id>/` | Cancel booking |

## 🎨 UI/UX Features

- **Modern Dark Theme** - Professional dark color scheme
- **Responsive Design** - Works on all devices
- **EventNest Branding** - Event (blue) + Nest (green) logo
- **Status Timeline** - Visual booking status tracker
- **Real-time Notifications** - Dropdown notification panel
- **Bangladesh Localization** - BDT currency (৳), +880 phone format

## 🔒 Security Features

- CSRF protection on all forms
- Login required for sensitive pages
- Password hashing
- Session management
- Input validation

## 📝 Sample Data

The project includes scripts to populate sample data:
- **5 Users** (including admin)
- **61 Services** across all categories
- **42 Store Products**
- **Sample Bookings, Orders, and Notifications**

## 🧪 Testing

```bash
# Run Django system check
python manage.py check

# Run tests
python manage.py test core
```

## 📦 Dependencies

```
Django>=5.0
Pillow>=10.0
python-dotenv>=1.0
```

## 🌐 Deployment

The project includes configuration for Vercel deployment:
- `vercel.json` - Vercel configuration
- `wsgi_vercel.py` - WSGI for serverless

## 👥 Authors

- **Prohar** - [GitHub](https://github.com/Prohar04)

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Django Framework
- Bootstrap Icons
- All contributors and testers
