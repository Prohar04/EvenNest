# Image Mapping Strategy & Management Command Documentation

## Overview

This document explains how images are connected to products and services in the EventNest Django project.

## 1. Models & Image Fields

Your project uses **7 main models** with image fields:

### Service Models (under `core.models`):

| Model | Image Field | Upload Path | Purpose |
|-------|------------|-------------|---------|
| `EventManagement` | `image` | `services/events/` | Event planning packages |
| `Photography` | `image` | `services/photography/` | Photography services |
| `Catering` | `image` | `services/catering/` | Catering services |
| `PrintingService` | `image` | `services/printing/` | Printing & design services |
| `Service` | `image` | `services/` | Generic marketplace services |
| `StoreItem` | `image` | `store/` | Physical products (decor, supplies) |

**Note**: The project currently has **NO data** in EventManagement, Photography, Catering, or PrintingService models, only in StoreItem (21 items).

## 2. Media Folder Structure

### Current Layout:
```
media/
├── services/
│   ├── event_management_1.jpeg
│   ├── event_management_1_5ooqnmO.jpeg
│   ├── event_management_2.jpeg
│   ├── photography_agency_1.jpeg
│   ├── photography_agency_2.jpeg
│   ├── catering_services_1.jpeg
│   ├── catering_services_2.jpeg
│   ├── card_printers_1.jpeg
│   ├── card_printers_2.jpeg
│   └── [other images]
│
└── store/
    ├── decor_items_1.jpeg
    ├── decor_items_2.jpeg
    ├── event_accesories_1.jpeg
    ├── event_accesories_2.jpeg
    ├── wedding_supply_1.jpeg
    ├── wedding_supply_2.jpeg
    └── [other images]
```

## 3. Image Mapping Strategy

The `assign_product_images` management command uses a **keyword-based intelligent mapping**:

### For StoreItems:
1. **Item Name Keywords** (highest priority):
   - "floral" → `decor_items_2.jpeg`
   - "light" → `event_accesories_2.jpeg`
   - "table" → `decor_items_1.jpeg`
   - "candle" → `decor_items_1.jpeg`
   - "balloon" → `event_accesories_2.jpeg`
   - "rose" → `decor_items_2.jpeg`
   - "gift" → `event_accesories_1.jpeg`
   - "prop" → `event_accesories_2.jpeg`

2. **Category Name** (fallback):
   - Category names like "Decor Items", "Event Accessories" are matched

3. **Default**: `decor_items_1.jpeg`

### For Services (EventManagement, Photography, Catering, Printing):
Similar keyword matching based on:
- Title words
- Service type / Shoot type / Cuisine type
- Pre-defined mapping dictionaries in the command

## 4. Management Command: `assign_product_images`

### Location:
```
core/management/commands/assign_product_images.py
```

### Usage:

**Dry run (preview changes without applying):**
```bash
python manage.py assign_product_images --dry-run --verbose
```

**Apply images to database:**
```bash
python manage.py assign_product_images
```

**Apply with detailed progress:**
```bash
python manage.py assign_product_images --verbose
```

### What the Command Does:

1. Scans all products/services in the database
2. Uses the `ImageMapper` class to determine which image each product should use
3. Compares current image field with proposed image path
4. Updates the database with new image paths (if running without `--dry-run`)
5. Prints a summary of changes

### Output Example:
```
Processing StoreItem...
  StoreItem: LED String Lights - Warm White - 10 Meters -> store/event_accesories_2.jpeg
  StoreItem: Fresh Red Roses Bundle - 50 Stems -> store/decor_items_2.jpeg
  
=== Image Assignment Summary ===
storeitem            | Total:  21 | Updated:  21

Total Records: 21 | Total Updated: 21
```

## 5. Current Status

✅ **Completed**:
- Management command created
- 21 StoreItems assigned images
- Mapping strategy tested

⚠️ **No Service Data Yet**:
- EventManagement: 0 records
- Photography: 0 records
- Catering: 0 records
- PrintingService: 0 records

These models will receive images automatically when products are added (either via fixtures or admin panel).

## 6. How to Add More Images

### Step 1: Add Image Files
Place image files in the appropriate media folder:
- Service images → `media/services/` or subdirectories
- Store items → `media/store/`

Use consistent naming: `{category}_{type}_{number}.{ext}`

### Step 2: Update Mapping (Optional)
Edit the `ImageMapper` class in `assign_product_images.py` to add new keywords/mappings:

```python
def map_store_item(self, item):
    name_keywords = {
        'your_keyword': 'media_file_name.jpg',
        # ... add more
    }
```

### Step 3: Run Command
```bash
python manage.py assign_product_images --verbose
```

## 7. Django Settings Configuration

Your settings are already configured correctly:

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

URLs configuration (urls.py) should include:
```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 8. Notes for Future Development

1. **Batch Image Assignment**: Run the command after loading fixture data
2. **Custom Mapping**: Modify the `ImageMapper` class for specific business logic
3. **Image Validation**: Consider adding image existence checks before assignment
4. **Admin Interface**: Images can also be uploaded directly via Django admin
5. **Thumbnails**: Consider using Pillow to generate thumbnails for faster loading

## 9. Troubleshooting

### Command not found?
```bash
# Make sure __init__.py files exist in management directories
touch core/management/__init__.py
touch core/management/commands/__init__.py
```

### Images not appearing?
1. Check MEDIA_URL and MEDIA_ROOT in settings.py
2. Verify image files exist in media folder
3. Run: `python manage.py assign_product_images --verbose`
4. Check database directly: View product in admin to see assigned image path

### Want to reset all images?
Update command with a `--reset` option or manually update database:
```bash
python manage.py shell
# Then in shell:
from core.models import StoreItem
StoreItem.objects.all().update(image='')
```
