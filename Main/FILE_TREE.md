# EvenNest Codebase File Tree

```
EvenNest/
└── Main/
    ├── .github/
    │   └── copilot-instructions.md          # AI agent instructions for the project
    │
    ├── .env                                  # Local environment variables (empty by default)
    ├── .env.vercel.example                   # Template for Vercel environment variables
    ├── .gitignore                            # Git ignore rules
    │
    ├── core/                                 # Main Django application
    │   ├── __init__.py
    │   ├── admin.py                         # Django admin configuration
    │   ├── apps.py
    │   ├── forms.py                         # Django forms (SignUp, Booking, etc.)
    │   ├── models.py                        # Database models (Service, Cart, Order, etc.)
    │   ├── tests.py
    │   ├── views.py                         # View functions (homepage, services, cart, etc.)
    │   ├── middleware.py                    # WebSocket middleware for authentication
    │   │
    │   ├── fixtures/
    │   │   ├── initial_products.json        # Seed data: 55+ services, 40+ store items
    │   │   └── README.md                    # Fixture documentation
    │   │
    │   ├── management/
    │   │   ├── __init__.py
    │   │   └── commands/
    │   │       ├── __init__.py
    │   │       └── assign_product_images.py # Management command to assign images
    │   │
    │   ├── migrations/                      # Database migration files
    │   │   ├── __init__.py
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_userprofile.py
    │   │   ├── 0003_remove_userprofile_unique_id.py
    │   │   ├── 0004_catering_eventmanagement_photography_printingservice.py
    │   │   ├── 0005_add_store_categories.py
    │   │   ├── 0006_cart_cartitem_order_orderitem_order_items.py
    │   │   ├── 0007_alter_service_title_alter_servicecategory_name_and_more.py
    │   │   ├── 0008_wishlist.py
    │   │   ├── 0009_chat_message_chat_core_chat_last_me_0513ff_idx_and_more.py
    │   │   ├── 0010_chatsession.py
    │   │   ├── 0011_booking.py
    │   │   ├── 0012_rename_core_bookin_service_5c7d5a_idx_core_bookin_service_c5dd06_idx_and_more.py
    │   │   ├── 0013_chat_admin_chat_subject_and_more.py
    │   │   ├── 0014_conversation_conversationmessage_and_more.py
    │   │   └── 0015_remove_chat_models.py  # Removed Chat/Message models
    │   │
    │   ├── static/
    │   │   └── css/
    │   │       └── style.css                # Custom CSS (400+ lines, design system)
    │   │
    │   ├── templates/
    │   │   ├── base.html                    # Master template
    │   │   ├── home.html
    │   │   ├── navbar_new.html              # Main navigation bar (updated)
    │   │   ├── navbar.html                  # Old navbar (updated)
    │   │   ├── search_results.html
    │   │   │
    │   │   ├── core/
    │   │   │   ├── navbar.html              # Core app navbar (updated)
    │   │   │   ├── booking_form.html
    │   │   │   ├── booking_list.html
    │   │   │   └── navbar.html
    │   │   │
    │   │   ├── registration/
    │   │   │   ├── auth_navbar.html
    │   │   │   ├── login.html
    │   │   │   ├── personal_info.html
    │   │   │   └── signup.html
    │   │   │
    │   │   └── services/
    │   │       ├── all_services.html        # Grid of services with 250px images
    │   │       ├── category.html
    │   │       ├── detail.html              # Service detail with 400px images
    │   │       └── ... (other service templates)
    │   │
    │   └── templatetags/
    │       ├── __init__.py
    │       ├── cart_tags.py                 # Custom template tags for cart
    │       └── __pycache__/
    │
    ├── media/                               # User-uploaded media files
    │   ├── services/                        # Service images
    │   │   ├── catering/
    │   │   ├── events/
    │   │   ├── photography/
    │   │   └── printing/
    │   └── store/                           # Store item images
    │
    ├── myproject/                           # Django project configuration
    │   ├── __init__.py
    │   ├── asgi.py                          # ASGI config (WebSocket/Channels)
    │   ├── settings.py                      # Django settings (265 lines)
    │   ├── urls.py                          # URL routing configuration
    │   ├── wsgi.py                          # WSGI config (local development)
    │   └── wsgi_vercel.py                   # WSGI config (Vercel serverless)
    │
    ├── staticfiles/                         # Collected static files
    │   ├── admin/
    │   │   ├── css/
    │   │   ├── img/
    │   │   └── js/
    │   └── css/
    │       └── style.css
    │
    ├── venv/                                # Virtual environment (not in git)
    │
    ├── db.sqlite3                           # SQLite database (development)
    ├── manage.py                            # Django management script
    ├── requirements.txt                     # Python dependencies (pip packages)
    │
    ├── vercel.json                          # Vercel deployment configuration
    ├── .gitignore                           # Git ignore patterns
    │
    ├── README.md                            # Basic project README
    ├── README_PROJECT_SUMMARY.md            # Comprehensive project summary
    ├── PROJECT_COMPLETION_STATUS.md         # Detailed completion status
    ├── MODELS_AND_FIXTURE_GUIDE.md          # Database models documentation
    ├── SEED_DATA_SUMMARY.md                 # Fixture data documentation
    ├── CHAT_IMPLEMENTATION_SUMMARY.md       # Chat system documentation (outdated)
    ├── CHAT_FIX_REPORT.md                   # Chat system fixes
    ├── IMAGE_MAPPING_GUIDE.md               # Image assignment documentation
    ├── TESTING_CHECKLIST.md                 # Testing procedures
    ├── AWS_SETUP_GUIDE.md                   # AWS RDS & S3 setup instructions
    ├── VERCEL_DEPLOYMENT_GUIDE.md           # Detailed Vercel deployment guide
    ├── VERCEL_QUICK_DEPLOY.md               # Quick 2-minute Vercel deployment
    │
    ├── create_admin.py                      # Script to create admin user
    ├── setup_admin.py                       # Alternative admin setup script
    └── verify_seed_data.py                  # Script to verify seed data loaded

```

---

## Directory Structure Summary

### Core Directories

| Directory | Purpose | Files |
|-----------|---------|-------|
| **core/** | Main Django app with models, views, templates | 15+ |
| **myproject/** | Django project settings & configuration | 5 |
| **media/** | User-uploaded service & store images | Dynamic |
| **staticfiles/** | Collected CSS, JS, admin assets | Dynamic |
| **.github/** | GitHub-specific files (CI/CD, instructions) | 1 |

### Key Files by Category

#### Configuration Files
- `myproject/settings.py` - Django configuration (265 lines)
- `myproject/asgi.py` - WebSocket/Channels setup
- `myproject/urls.py` - URL routing
- `myproject/wsgi.py` / `wsgi_vercel.py` - WSGI application
- `vercel.json` - Vercel serverless config
- `requirements.txt` - All Python dependencies

#### Models & Database
- `core/models.py` - 13+ database models
- `core/migrations/` - 15 migration files
- `db.sqlite3` - Development database

#### Views & Logic
- `core/views.py` - 587 lines of view functions
- `core/forms.py` - Django form classes
- `core/admin.py` - Admin panel configuration
- `core/middleware.py` - WebSocket middleware

#### Templates
- `core/templates/base.html` - Master template
- `core/templates/navbar_new.html` - Main navigation
- `core/templates/services/` - Service browsing
- `core/templates/store/` - Store browsing
- `core/templates/registration/` - Auth pages
- `core/templates/core/` - App-specific templates

#### Styling
- `core/static/css/style.css` - 400+ lines custom CSS

#### Documentation
- `README_PROJECT_SUMMARY.md` - Full project overview
- `PROJECT_COMPLETION_STATUS.md` - Implementation details
- `AWS_SETUP_GUIDE.md` - AWS deployment instructions
- `VERCEL_QUICK_DEPLOY.md` - Quick deployment guide
- `MODELS_AND_FIXTURE_GUIDE.md` - Database schema

#### Management & Data
- `core/fixtures/initial_products.json` - 63 seed data entries
- `core/management/commands/assign_product_images.py` - Image setup
- `requirements.txt` - 130+ Python packages
- `manage.py` - Django CLI

---

## Statistics

| Metric | Count |
|--------|-------|
| **Python Files** | 20+ |
| **HTML Templates** | 20+ |
| **CSS Lines (Custom)** | 400+ |
| **Database Tables** | 13+ |
| **Migrations** | 15 |
| **Service Models** | 6 (Event, Photo, Catering, Printing, Service) |
| **Store Models** | 2 (StoreItem, StoreCategory) |
| **User Models** | 1 (UserProfile) |
| **Commerce Models** | 4 (Cart, Order, Wishlist, Booking) |
| **Dependencies (Packages)** | 130+ |
| **Total Seed Data Items** | 63 |
| **Documentation Files** | 10+ |

---

## Key Files to Understand the Project

1. **Start here:** `README_PROJECT_SUMMARY.md` - Project overview
2. **Architecture:** `core/models.py` - Database schema
3. **Views:** `core/views.py` - Business logic
4. **Settings:** `myproject/settings.py` - Configuration
5. **Data:** `core/fixtures/initial_products.json` - Seed data
6. **Deploy:** `AWS_SETUP_GUIDE.md` + `VERCEL_QUICK_DEPLOY.md`

---

## Technology Stack Location

| Technology | Files |
|-----------|-------|
| **Django 5.2** | `requirements.txt`, `manage.py` |
| **Django Channels** | `myproject/asgi.py`, `core/middleware.py` |
| **Bootstrap 5** | `core/templates/base.html` |
| **SQLite/PostgreSQL** | `myproject/settings.py`, `db.sqlite3` |
| **AWS S3** | `myproject/settings.py` (S3 config) |
| **Vercel Serverless** | `vercel.json`, `myproject/wsgi_vercel.py` |

---

*Generated: December 8, 2025*  
*Python 3.13 | Django 5.2rc1 | Channels 4.x*
