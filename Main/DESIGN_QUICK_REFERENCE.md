# 🎨 EvenNest Design System - Quick Reference Card

## Color Palette

### Primary Gradient (Purple → Indigo)
```
Start Color:  #667eea (Soft Purple)
End Color:    #764ba2 (Deep Indigo)
Direction:    135deg (diagonal)
CSS:          linear-gradient(135deg, #667eea 0%, #764ba2 100%)
Usage:        Primary buttons, hero sections, links, main brand color
```

### Success Gradient (Cyan → Light Blue)
```
Start Color:  #4facfe (Bright Cyan)
End Color:    #00f2fe (Neon Cyan)
Direction:    135deg (diagonal)
CSS:          linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)
Usage:        Success badges, success buttons, positive states
```

### Danger/Warm Gradient (Rose → Gold)
```
Start Color:  #fa709a (Rose Pink)
End Color:    #fee140 (Warm Gold)
Direction:    135deg (diagonal)
CSS:          linear-gradient(135deg, #fa709a 0%, #fee140 100%)
Usage:        Alerts, warnings, danger states, error messages
```

### Info Gradient (Mint → Rose)
```
Start Color:  #a8edea (Soft Mint)
End Color:    #fed6e3 (Light Pink)
Direction:    135deg (diagonal)
CSS:          linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)
Usage:        Info badges, informational sections
```

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| H1      | Inter | 56px | 700 | #212529 |
| H2      | Inter | 48px | 700 | #212529 |
| H3      | Inter | 40px | 700 | #212529 |
| H4      | Inter | 32px | 700 | #212529 |
| H5      | Inter | 28px | 700 | #212529 |
| Body    | Inter | 16px | 400 | #495057 |
| Small   | Inter | 14px | 400 | #6c757d |
| Muted   | Inter | 14px | 400 | #6c757d |

---

## Spacing Scale

```
xs  = 0.25rem = 4px
sm  = 0.5rem  = 8px
md  = 1rem    = 16px
lg  = 1.5rem  = 24px
xl  = 2rem    = 32px
2xl = 3rem    = 48px
```

---

## Shadow System

### Soft Shadow (Cards)
```css
box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
```

### Medium Shadow (Hover Cards)
```css
box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
```

### Hard Shadow (Modals)
```css
box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
```

---

## Border Radius

| Size | Pixels | Usage |
|------|--------|-------|
| sm   | 4px    | Small elements |
| md   | 8px    | Form inputs |
| lg   | 12px   | Cards, buttons |
| xl   | 16px   | Large cards, sections |
| full | 9999px | Buttons, badges |

---

## Animations

| Name | Duration | Easing | Effect |
|------|----------|--------|--------|
| Fast | 150ms | cubic-bezier(0.4, 0, 0.2, 1) | Quick interactions |
| Base | 300ms | cubic-bezier(0.4, 0, 0.2, 1) | Standard transitions |
| Slow | 500ms | cubic-bezier(0.4, 0, 0.2, 1) | Page transitions |

### Key Animations

**slideIn** - Content appears from bottom
```css
@keyframes slideIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
```

**slideInRight** - Notifications from right
```css
@keyframes slideInRight {
    from { transform: translateX(100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}
```

**slideInDown** - Header from top
```css
@keyframes slideInDown {
    from { transform: translateY(-100%); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}
```

---

## Component Quick Reference

### Buttons

```html
<!-- Primary Button -->
<button class="btn btn-primary">Primary Button</button>

<!-- Secondary Button -->
<button class="btn btn-secondary">Secondary Button</button>

<!-- Outline Button -->
<button class="btn btn-outline">Outline Button</button>

<!-- Success Button -->
<button class="btn btn-success">Success Button</button>

<!-- Danger Button -->
<button class="btn btn-danger">Danger Button</button>

<!-- With Icon -->
<button class="btn btn-primary">
    <i class="bi bi-download"></i> Download
</button>

<!-- Size Variants -->
<button class="btn btn-sm btn-primary">Small</button>
<button class="btn btn-primary">Default</button>
<button class="btn btn-lg btn-primary">Large</button>
```

### Cards

```html
<div class="card hover-lift">
    <div class="card-img-wrapper">
        <img src="image.jpg" alt="...">
        <div class="card-price">$99.99</div>
    </div>
    <div class="card-body">
        <h5 class="card-title">Title</h5>
        <p class="card-text">Description</p>
    </div>
    <div class="card-footer">
        <button class="btn btn-primary w-100">Action</button>
    </div>
</div>
```

### Forms

```html
<form>
    <div class="form-group">
        <label for="input" class="form-label">Field Label</label>
        <input type="text" id="input" class="form-control" placeholder="Placeholder">
    </div>
    <button type="submit" class="btn btn-primary w-100">Submit</button>
</form>
```

### Alerts

```html
<!-- Success -->
<div class="alert alert-success">
    <i class="bi bi-check-circle"></i> Success message
</div>

<!-- Error -->
<div class="alert alert-danger">
    <i class="bi bi-exclamation-circle"></i> Error message
</div>

<!-- Info -->
<div class="alert alert-info">
    <i class="bi bi-info-circle"></i> Info message
</div>

<!-- Warning -->
<div class="alert alert-warning">
    <i class="bi bi-exclamation-triangle"></i> Warning message
</div>
```

### Badges

```html
<span class="badge badge-primary">Primary</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-danger">Danger</span>
<span class="badge badge-info">Info</span>
<span class="badge badge-warm">Warm</span>
```

---

## Responsive Breakpoints

```css
/* Mobile First */
/* <576px = Extra Small (Default) */

/* 576px and up = Small */
@media (min-width: 576px) { ... }

/* 768px and up = Medium (Tablet) */
@media (min-width: 768px) { ... }

/* 992px and up = Large */
@media (min-width: 992px) { ... }

/* 1200px and up = Extra Large (Desktop) */
@media (min-width: 1200px) { ... }

/* 1400px and up = XXL */
@media (min-width: 1400px) { ... }
```

---

## Contact Form Integration

### Simple Button
```html
<a href="{% url 'contact_provider' %}" class="btn btn-primary">
    <i class="bi bi-envelope"></i> Contact Us
</a>
```

### With Service Pre-fill
```html
<a href="{% url 'contact_provider' %}?service_type=event&service_id={{ service.id }}&service_name={{ service.title }}" 
   class="btn btn-primary">
    Contact Provider
</a>
```

### Service Type Options
```
event       = Event Management
photo       = Photography
catering    = Catering
printing    = Printing Service
store       = Store Item
general     = General Inquiry
```

---

## CSS Variables (Root)

```css
:root {
    /* Gradients */
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --gradient-success: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --gradient-danger: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    --gradient-info: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    
    /* Timing */
    --micro-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
    --micro-base: 300ms cubic-bezier(0.4, 0, 0.2, 1);
    --micro-slow: 500ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

---

## Common Color Values

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Primary | #667eea | 102, 126, 234 | Main brand |
| Success | #4facfe | 79, 172, 254 | Positive |
| Danger | #fa709a | 250, 112, 154 | Negative |
| Warning | #ffc107 | 255, 193, 7 | Caution |
| Gray 300 | #dee2e6 | 222, 226, 230 | Borders |
| Gray 600 | #6c757d | 108, 117, 125 | Muted text |
| Gray 900 | #212529 | 33, 37, 41 | Dark text |
| White | #ffffff | 255, 255, 255 | Background |

---

## Hover & Focus States

### Button Hover
```css
.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
}
```

### Card Hover
```css
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
}
```

### Form Input Focus
```css
input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}
```

---

## Mobile-First Strategy

1. **Base Styles:** Mobile (< 576px)
2. **Tablet:** @media (min-width: 768px)
3. **Desktop:** @media (min-width: 1200px)

**Mobile Optimizations:**
- Full-width buttons
- Stacked layouts
- Compact padding
- Larger touch targets (44px min)
- Single column grid

---

## Accessibility Features

✅ **Color Contrast**
- WCAG AA compliant (4.5:1 minimum)
- Text color on gradients >= 7:1

✅ **Focus States**
- Visible focus indicators
- 2px outline or 4px glow

✅ **Touch Targets**
- Minimum 44px × 44px
- Mobile buttons full-width

✅ **Semantic HTML**
- Proper heading hierarchy
- Form labels for all inputs
- ARIA labels where needed

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Modern CSS | `/core/static/css/modern-design.css` | Design system |
| Contact Form | `/core/templates/core/contact_provider.html` | Form page |
| Success Page | `/core/templates/core/contact_success.html` | Confirmation |
| Guide | `/CONTACT_MODERN_DESIGN_GUIDE.md` | Full documentation |
| Examples | `/CONTACT_BUTTON_EXAMPLES.html` | Code snippets |
| Checklist | `/SETUP_CHECKLIST_CONTACT_DESIGN.md` | Setup tasks |

---

## Quick Commands

```bash
# Start server
python manage.py runserver

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Access admin
# http://localhost:8000/admin/

# Access contact form
# http://localhost:8000/contact-provider/
```

---

## Pro Tips

💡 **Tip 1:** Use CSS variables for consistent styling
```css
color: var(--color-primary);
```

💡 **Tip 2:** Combine multiple classes for flexibility
```html
<button class="btn btn-primary btn-lg">Large Primary Button</button>
```

💡 **Tip 3:** Use utility classes for quick customization
```html
<div class="hover-lift shadow-lg rounded-xl">Custom Card</div>
```

💡 **Tip 4:** Test responsiveness in DevTools
```
F12 → Toggle device toolbar → Select device
```

💡 **Tip 5:** Clear cache when updating CSS
```
Ctrl+Shift+Delete → Select "Cached images and files" → Clear
```

---

## Related Documentation

- 📖 **Full Guide:** `CONTACT_MODERN_DESIGN_GUIDE.md`
- 💻 **Code Examples:** `CONTACT_BUTTON_EXAMPLES.html`
- ✅ **Setup Guide:** `SETUP_CHECKLIST_CONTACT_DESIGN.md`
- 📝 **Summary:** `IMPLEMENTATION_SUMMARY.md`

---

**Quick Reference Card v1.0**  
Last Updated: December 8, 2025  
Django 5.2 | Bootstrap 5.3 | Python 3.11+
