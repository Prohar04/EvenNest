# EventNest Project Structure

```
EventNest/
│
├── Main/                               # Production Django Application
│   ├── manage.py                       # Django management utility
│   ├── requirements.txt                # Python dependencies
│   ├── db.sqlite3                      # SQLite database
│   ├── vercel.json                     # Vercel deployment config
│   │
│   ├── core/                           # Main Django App
│   │   ├── models.py                   # Database models (Service, StoreItem, Chat, etc.)
│   │   ├── views.py                    # View functions and logic
│   │   ├── forms.py                    # Django forms
│   │   ├── admin.py                    # Django admin configuration
│   │   ├── urls.py                     # URL routing
│   │   ├── middleware.py               # Custom middleware
│   │   ├── apps.py                     # App configuration
│   │   ├── tests.py                    # Unit tests
│   │   │
│   │   ├── fixtures/                   # Initial data
│   │   │   └── initial_products.json   # Seed data (59 products)
│   │   │
│   │   ├── management/                 # Custom management commands
│   │   ├── migrations/                 # Database migrations (0001-0015)
│   │   │
│   │   ├── templates/                  # HTML Templates
│   │   │   ├── base.html               # Master template
│   │   │   ├── footer.html             # Footer component
│   │   │   ├── navbar.html             # Navigation bar
│   │   │   ├── home.html               # Homepage
│   │   │   ├── registration/
│   │   │   │   ├── login.html
│   │   │   │   └── signup.html
│   │   │   ├── services/
│   │   │   │   ├── all_services.html   # Services grid view
│   │   │   │   ├── service_detail.html # Service detail page
│   │   │   │   └── category.html       # Category filter view
│   │   │   ├── store/
│   │   │   │   ├── all_items.html      # Store grid view
│   │   │   │   ├── item_detail.html    # Item detail page
│   │   │   │   └── cart.html           # Shopping cart
│   │   │   ├── chat/
│   │   │   │   ├── chat_list.html      # Conversation list
│   │   │   │   └── chat_detail.html    # Chat interface
│   │   │   ├── account/
│   │   │   │   ├── profile.html
│   │   │   │   └── wishlist.html
│   │   │   └── errors/
│   │   │       ├── 404.html
│   │   │       └── 500.html
│   │   │
│   │   ├── static/                     # Static files (CSS, JS, Images)
│   │   │   ├── css/
│   │   │   │   ├── style.css           # Main stylesheet (optimized)
│   │   │   │   ├── modern-design.css   # Modern UI components
│   │   │   │   └── animations.css      # Animation definitions
│   │   │   ├── js/
│   │   │   │   ├── cart.js             # Cart functionality
│   │   │   │   ├── search.js           # Search functionality
│   │   │   │   └── utils.js            # Utility functions
│   │   │   └── images/
│   │   │       ├── logo.png
│   │   │       └── favicon.ico
│   │   │
│   │   └── __pycache__/                # Python cache (auto-generated)
│   │
│   ├── myproject/                      # Django Project Config
│   │   ├── settings.py                 # Django settings (production-ready)
│   │   ├── urls.py                     # Main URL router
│   │   ├── wsgi.py                     # WSGI application
│   │   ├── asgi.py                     # ASGI for WebSocket (Channels)
│   │   └── __init__.py
│   │
│   ├── media/                          # User-uploaded files
│   │   ├── services/                   # Service images (41 images)
│   │   └── store/                      # Store item images (29 images)
│   │
│   ├── staticfiles/                    # Collected static files (production)
│   │
│   ├── .env                            # Environment variables (not committed)
│   ├── .env.local                      # Local dev template
│   ├── .env.production                 # Production template
│   ├── .gitignore                      # Git ignore rules
│   │
│   └── Documentation/                  # Project Documentation
│       ├── README.md                   # Main readme
│       ├── QUICKSTART.md               # 5-minute setup guide
│       ├── ACTION_ITEMS.md             # Setup checklist
│       ├── VERCEL_DEPLOYMENT_COMPLETE_GUIDE.md
│       ├── VERCEL_DEPLOYMENT_READY.md
│       ├── CHAT_FIX_REPORT.md
│       ├── PROJECT_COMPLETION_STATUS.md
│       └── [30+ other guides]
│
├── .git/                               # Git repository
├── .github/
│   └── copilot-instructions.md        # AI assistant guidelines
│
└── Root Files
    ├── vercel.json                     # Vercel deployment config
    ├── requirements.txt                # Dependencies
    └── manage.py                       # Django CLI
```

## Key Directories Explained

### 📦 **Core Application (`core/`)**
- **Models**: Service, StoreItem, Chat, User profiles, Orders, Bookings
- **Views**: All request handlers and business logic
- **Templates**: 20+ HTML files for all pages
- **Static**: Optimized CSS (1384 lines), Bootstrap integration, Bootstrap Icons
- **Media**: 70 product images (41 services + 29 store items)

### 🎨 **Frontend**
- **Base Template**: Master layout with animated gradient background
- **Responsive Design**: Mobile-first, tested on all devices
- **Bootstrap 5**: Component framework
- **Bootstrap Icons**: 6000+ SVG icons
- **Custom CSS**: Professional gradients, animations, transitions

### 🗄️ **Database**
- **SQLite** (local): Fast, no setup required
- **MySQL** (production): Aiven cloud database via `DATABASE_URL`
- **Migrations**: 15 versioned schema changes
- **Seed Data**: 59 products (30 services + 21 store items + 8 categories)

### ⚙️ **Configuration**
- **settings.py**: Smart environment detection (DEBUG, DATABASE, ALLOWED_HOSTS)
- **wsgi.py**: Production WSGI server
- **asgi.py**: WebSocket support via Django Channels
- **vercel.json**: Serverless deployment config

### 📱 **Real-Time Features**
- **WebSocket Chat**: Django Channels integration
- **Live Messaging**: Real-time conversation updates
- **Presence Tracking**: Online/offline status
- **Admin Inbox**: Centralized message management

---

## Performance Optimizations

✅ **CSS Optimization**
- Minified & organized selectors
- CSS variables for maintainability
- Hardware acceleration with `will-change`
- Optimized animations (GPU-accelerated)

✅ **JavaScript**
- Lazy loading for images
- Deferred script loading
- Event delegation for dynamic elements
- Minimal dependencies (Bootstrap only)

✅ **Network**
- DNS prefetch for CDNs
- Preload critical assets
- Gzip compression enabled
- Static file caching headers

✅ **Database**
- Indexed fields for fast queries
- Optimized models
- Efficient relationships
- Connection pooling ready

---

## File Statistics

| Section | Count | Size |
|---------|-------|------|
| **Templates** | 20+ | ~50 KB |
| **CSS Files** | 2 | ~51 KB |
| **JavaScript** | 1 | ~5 KB |
| **Product Images** | 70 | ~15 MB |
| **Database** | 1 | ~1 MB |
| **Migrations** | 15 | ~20 KB |
| **Total Code** | 300+ | ~10 MB |

---

## Technology Stack

**Backend**: Django 5.2rc1, Python 3.11
**Database**: SQLite (dev) / MySQL (production)
**Frontend**: Bootstrap 5, HTML5, CSS3
**Real-Time**: Django Channels, Daphne
**Deployment**: Vercel, Aiven MySQL
**Package Manager**: Pip

---

## Quick Links

- 📖 **Setup**: `QUICKSTART.md`
- 🚀 **Deploy**: `VERCEL_DEPLOYMENT_COMPLETE_GUIDE.md`
- 💬 **Chat**: See `CHAT_FIX_REPORT.md`
- 🎨 **Design**: See `FINAL_VERIFICATION_CHECKLIST.md`

