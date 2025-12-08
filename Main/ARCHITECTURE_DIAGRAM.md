# 🏗️ EvenNest Contact & Design System - Architecture Diagram

## System Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE LAYER                          │
├──────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  ┌─────────────────────┐  ┌──────────────────┐  ┌──────────────────┐ │
│  │   Contact Form      │  │  Service Pages   │  │   Store Pages    │ │
│  │  (contact_provider  │  │  (all_services   │  │  (all_store      │ │
│  │   .html)            │  │   .html)         │  │   .html)         │ │
│  │                     │  │                  │  │                  │ │
│  │ • Hero Section      │  │ • Service Cards  │  │ • Item Cards     │ │
│  │ • Contact Form      │  │ • Contact Btn    │  │ • Contact Btn    │ │
│  │ • Info Boxes        │  │ • Details Link   │  │ • Add to Cart    │ │
│  │ • Validation Msgs   │  │                  │  │                  │ │
│  └─────────────────────┘  └──────────────────┘  └──────────────────┘ │
│           ↓                        ↓                      ↓            │
│    [Contact Form]          [Contact Btn]           [Contact Btn]      │
│                                                                        │
│  ┌─────────────────────┐                                              │
│  │  Success Page       │                                              │
│  │  (contact_success   │                                              │
│  │   .html)            │                                              │
│  │                     │                                              │
│  │ • Animated Icon     │                                              │
│  │ • Confirmation      │                                              │
│  │ • Action Buttons    │                                              │
│  └─────────────────────┘                                              │
│                                                                        │
└──────────────────────────────────────────────────────────────────────┘
                                    ↓
┌──────────────────────────────────────────────────────────────────────┐
│                      STYLING LAYER (CSS)                              │
├──────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  style.css (721 lines)          modern-design.css (520 lines)        │
│  ├─ Bootstrap overrides         ├─ Color gradients                   │
│  ├─ Chart styling               ├─ Button styles                     │
│  ├─ Navbar customization        ├─ Card components                   │
│  ├─ Cart/Order styling          ├─ Form elements                     │
│  ├─ Chat interface              ├─ Animations                        │
│  └─ Existing components         ├─ Responsive design                 │
│                                 └─ Utility classes                   │
│                                                                        │
│  Color System:                                                        │
│  ├─ Primary Gradient   (#667eea → #764ba2)                          │
│  ├─ Success Gradient   (#4facfe → #00f2fe)                          │
│  ├─ Danger Gradient    (#fa709a → #fee140)                          │
│  └─ Info Gradient      (#a8edea → #fed6e3)                          │
│                                                                        │
│  Animation System:                                                    │
│  ├─ Fast (150ms)      - Micro interactions                           │
│  ├─ Base (300ms)      - Standard transitions                         │
│  └─ Slow (500ms)      - Page transitions                             │
│                                                                        │
└──────────────────────────────────────────────────────────────────────┘
                                    ↓
┌──────────────────────────────────────────────────────────────────────┐
│                    BACKEND LOGIC LAYER (Django)                       │
├──────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  VIEWS (views.py)                                                     │
│  ├─ contact_provider()                                               │
│  │  ├─ GET: Display form                                             │
│  │  ├─ Pre-fill: user data, service info                             │
│  │  └─ POST: Save Contact, redirect to success                       │
│  │                                                                    │
│  └─ contact_success()                                                │
│     └─ Display confirmation page                                     │
│                                                                        │
│  FORMS (forms.py)                                                     │
│  └─ ContactForm                                                      │
│     ├─ full_name (CharField)                                         │
│     ├─ email (EmailField)                                            │
│     ├─ phone (CharField) - optional                                  │
│     ├─ subject (CharField)                                           │
│     ├─ message (TextField)                                           │
│     ├─ preferred_contact_method (ChoiceField)                        │
│     └─ service_type (ChoiceField)                                    │
│                                                                        │
│  MODELS (models.py)                                                   │
│  └─ Contact                                                          │
│     ├─ user (ForeignKey, optional)                                   │
│     ├─ full_name (CharField)                                         │
│     ├─ email (EmailField)                                            │
│     ├─ phone (CharField)                                             │
│     ├─ subject (CharField)                                           │
│     ├─ message (TextField)                                           │
│     ├─ preferred_contact_method (CharField)                          │
│     ├─ service_type (CharField)                                      │
│     ├─ service_id (IntegerField)                                     │
│     ├─ service_name (CharField)                                      │
│     ├─ status (CharField)  [New/Read/Responded]                      │
│     └─ timestamps (created_at, updated_at)                           │
│                                                                        │
│  ADMIN (admin.py)                                                     │
│  └─ ContactAdmin                                                     │
│     ├─ list_display: [name, email, type, status, date]               │
│     ├─ list_filter: [status, service_type, created_at]               │
│     ├─ search_fields: [name, email, subject]                         │
│     └─ fieldsets: [Info, Details, Preferences, Timestamps]           │
│                                                                        │
└──────────────────────────────────────────────────────────────────────┘
                                    ↓
┌──────────────────────────────────────────────────────────────────────┐
│                      DATABASE LAYER (SQLite)                          │
├──────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  core_contact (Table)                                                │
│  ├─ id (PK)                                                          │
│  ├─ user_id (FK)                                                     │
│  ├─ full_name (VARCHAR)                                              │
│  ├─ email (VARCHAR)                                                  │
│  ├─ phone (VARCHAR)                                                  │
│  ├─ subject (VARCHAR)                                                │
│  ├─ message (TEXT)                                                   │
│  ├─ preferred_contact_method (VARCHAR)                               │
│  ├─ service_type (VARCHAR)                                           │
│  ├─ service_id (INT)                                                 │
│  ├─ service_name (VARCHAR)                                           │
│  ├─ status (VARCHAR)                                                 │
│  ├─ created_at (DATETIME)                                            │
│  └─ updated_at (DATETIME)                                            │
│                                                                        │
│  Indexes:                                                             │
│  ├─ email                                                            │
│  ├─ created_at (DESC)                                                │
│  └─ service_type + service_id                                        │
│                                                                        │
└──────────────────────────────────────────────────────────────────────┘

```

---

## User Flow Diagram

```
START
  │
  ├─→ User visits ANY page
  │
  ├─→ [A] General Inquiry
  │   └─→ Click "Contact Us" button
  │       └─→ Navigate to /contact-provider/
  │
  ├─→ [B] Service Inquiry
  │   └─→ Click "Contact Provider" button on service card
  │       └─→ Navigate to /contact-provider/
  │           ?service_type=event&service_id=1&service_name=Wedding
  │
  ├─→ [C] Store Inquiry
  │   └─→ Click "Contact Seller" button on item
  │       └─→ Navigate to /contact-provider/
  │           ?service_type=store&service_id=5&service_name=Decoration
  │
  └─→ Contact Form Page Loads
     │
     ├─→ NOT Authenticated
     │   └─→ Form shows empty fields
     │       └─→ User fills: name, email, phone, subject, message
     │
     ├─→ Authenticated
     │   └─→ Form pre-filled: name, email, phone
     │       └─→ User modifies if needed, fills: subject, message
     │
     ├─→ IF Service Pre-fill
     │   └─→ Service info banner shows
     │       └─→ service_type pre-selected in dropdown
     │           └─→ service_name field populated
     │
     ├─→ User selects
     │   ├─→ preferred_contact_method (Email/Phone/WhatsApp/Other)
     │   ├─→ service_type (Event/Photo/Catering/Printing/Store/General)
     │   └─→ Completes message (max 500 chars)
     │
     ├─→ Validation (Client-Side)
     │   ├─→ Required fields check
     │   ├─→ Email format validation
     │   ├─→ Phone format validation
     │   └─→ Message length check
     │
     ├─→ User clicks "Send Message"
     │   │
     │   ├─→ [SUCCESS PATH]
     │   │   └─→ Form submits to /contact-provider/ (POST)
     │   │       └─→ Django validates (server-side)
     │   │           └─→ Creates Contact object in database
     │   │               └─→ Sets status = "New"
     │   │                   └─→ Redirects to /contact-success/
     │   │                       └─→ Shows confirmation page
     │   │                           └─→ Animated success icon
     │   │                               └─→ "Thank you" message
     │   │                                   └─→ Action buttons
     │   │                                       └─→ Back Home / Browse Services
     │   │
     │   └─→ [ERROR PATH]
     │       └─→ Validation fails
     │           └─→ Shows error messages above fields
     │               └─→ User corrects and retries
     │
     └─→ Admin Receives Contact
        └─→ Available at /admin/core/contact/
            └─→ Filter by status/service/date
                └─→ Read contact details
                    └─→ Update status (New → Read → Responded)
                        └─→ Contact business (email/phone/whatsapp)
                            └─→ Respond to user

END
```

---

## Data Flow - Contact Submission

```
┌─────────────────┐
│   Form Input    │
│                 │
│ • name          │
│ • email         │
│ • phone         │
│ • subject       │
│ • message       │
│ • method        │
│ • service_type  │
│ • service_id    │
└────────┬────────┘
         │
         ↓
┌─────────────────────────────┐
│   Client-Side Validation    │
│                             │
│ ✓ Required fields check     │
│ ✓ Email format regex        │
│ ✓ Phone format regex        │
│ ✓ Message length max 500    │
└────────┬────────────────────┘
         │ (if valid)
         ↓
┌──────────────────────────────────┐
│   HTTP POST Request              │
│   /contact-provider/             │
│                                  │
│   Headers:                       │
│   - Content-Type: form-data      │
│   - CSRF Token: [token]          │
│                                  │
│   Body: Form data                │
└────────┬─────────────────────────┘
         │
         ↓
┌──────────────────────────────────┐
│   Django Views Processing        │
│   contact_provider(request)      │
│                                  │
│ 1. Extract form data             │
│ 2. Create ContactForm instance   │
│ 3. Validate (server-side)        │
│ 4. If user authenticated:        │
│    - Link to user                │
│    - Auto-fill missing fields    │
└────────┬─────────────────────────┘
         │ (if valid)
         ↓
┌──────────────────────────────────┐
│   Save to Database               │
│   Contact.objects.create()       │
│                                  │
│ • user_id (if authenticated)     │
│ • full_name                      │
│ • email                          │
│ • phone                          │
│ • subject                        │
│ • message                        │
│ • preferred_contact_method       │
│ • service_type                   │
│ • service_id                     │
│ • service_name                   │
│ • status = 'new'                 │
│ • created_at = now()             │
│ • updated_at = now()             │
└────────┬─────────────────────────┘
         │ (success)
         ↓
┌──────────────────────────────────┐
│   Redirect to Success Page       │
│   /contact-success/              │
│                                  │
│ Show:                            │
│ • Success message                │
│ • Animated icon                  │
│ • Response time (24 hrs)         │
│ • Action buttons                 │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│   Admin Notification             │
│   Django Admin Interface         │
│                                  │
│ • New contact appears in list    │
│ • Can filter by status           │
│ • Can search by email/name       │
│ • Can mark as Read/Responded     │
│ • Can export data                │
└──────────────────────────────────┘
```

---

## Component Hierarchy

```
base.html (Template)
├── Head
│   ├── Bootstrap CSS
│   ├── Bootstrap Icons
│   ├── style.css (existing)
│   └── modern-design.css (NEW)
│
├── Body
│   ├── navbar.html
│   │   ├── Logo
│   │   ├── Nav Links
│   │   │   └── Contact (NEW - optional)
│   │   ├── Search Form
│   │   └── Account/Cart
│   │
│   ├── Main Content
│   │   ├── contact_provider.html (NEW)
│   │   │   ├── Hero Section (.hero-section)
│   │   │   ├── Contact Form (.contact-card)
│   │   │   │   ├── Service Info (.service-info-banner)
│   │   │   │   ├── Form Fields (.form-group)
│   │   │   │   ├── Character Counter
│   │   │   │   └── Buttons (.form-actions)
│   │   │   └── Info Boxes (.info-box)
│   │   │
│   │   └── contact_success.html (NEW)
│   │       ├── Success Container
│   │       ├── Success Icon (animated)
│   │       ├── Success Message
│   │       ├── Details (.success-details)
│   │       └── Action Buttons
│   │
│   └── Scripts
│       ├── Bootstrap JS
│       ├── Popper JS
│       └── Form Validation (inline in templates)

CSS Structure:
├── Bootstrap Framework
├── style.css (existing overrides)
└── modern-design.css (NEW design system)
    ├── :root (CSS variables)
    ├── Hero Sections (.hero-section)
    ├── Cards (.card, .card-img-wrapper)
    ├── Buttons (.btn variants)
    ├── Forms (.form-control, .form-group)
    ├── Alerts (.alert variants)
    ├── Badges (.badge variants)
    ├── Animations (@keyframes)
    ├── Links (a, .link-underline)
    ├── Utilities (.hover-*, .shadow-*, .rounded-*)
    └── Responsive (@media queries)
```

---

## Integration Points

```
Pages where Contact buttons should be added:

1. Service Detail Page (/services/detail/<id>/)
   └─ Add button: "Contact Provider"

2. Service Category Page (/services/<category>/)
   └─ Add button to each card: "Contact" or "Inquire"

3. Store Item Detail Page (/store/detail/<id>/)
   └─ Add button: "Contact Seller"

4. Store Category Page (/store/<category>/)
   └─ Add button to each card: "Contact"

5. Home Page (/)
   └─ Add hero section CTA: "Get in Touch"

6. Search Results (/search/)
   └─ Add button to each result: "Contact"

7. Navbar (all pages)
   └─ Add nav link: "Contact" (optional)

8. Footer (all pages)
   └─ Add link: "Contact Us"

Parameter Pattern:
/?service_type=[type]&service_id=[id]&service_name=[name]

Example URLs:
- /contact-provider/?service_type=event&service_id=1&service_name=Wedding
- /contact-provider/?service_type=photo&service_id=3&service_name=Portrait
- /contact-provider/?service_type=store&service_id=5&service_name=Decoration
```

---

## Technology Stack

```
Frontend:
├─ HTML5 (Semantic)
├─ CSS3 (Modern + Gradients)
│  ├─ Flexbox layouts
│  ├─ CSS Grid (optional)
│  ├─ CSS Variables
│  └─ Animations/Transitions
├─ JavaScript (Vanilla)
│  ├─ Form validation
│  ├─ Character counter
│  └─ Event handling
└─ Bootstrap 5.3
   └─ Grid system, utilities

Backend:
├─ Django 5.2rc1
│  ├─ Models (Contact)
│  ├─ Forms (ContactForm)
│  ├─ Views (contact_provider, contact_success)
│  ├─ URLs (routing)
│  ├─ Admin (ContactAdmin)
│  └─ Templates (HTML)
└─ Python 3.11+

Database:
├─ SQLite (local dev)
└─ PostgreSQL/MySQL (production)

Styling:
├─ CSS (custom)
└─ Bootstrap (framework)

Icons:
└─ Bootstrap Icons (bi class)

Font:
├─ Inter (primary)
├─ Segoe UI (fallback)
└─ System fonts (safe)
```

---

**Last Updated:** December 8, 2025  
**Version:** 1.0  
**Status:** Production Ready
