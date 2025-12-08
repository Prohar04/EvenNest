# EventNest Models & Fixture Structure Guide

## COMPLETE MODEL REFERENCE

### 1. SERVICE MODELS

#### ServiceCategory
```
pk: integer (primary key)
name: CharField(max_length=100)
description: TextField(blank=True)
```

#### Service (Generic)
```
pk: integer (primary key)
category: ForeignKey(ServiceCategory)
title: CharField(max_length=200)
description: TextField()
price: DecimalField(max_digits=10, decimal_places=2)
image: ImageField(upload_to='services/')
created_at: DateTimeField(auto_now_add=True)
updated_at: DateTimeField(auto_now=True)
```

#### EventManagement
```
pk: integer (primary key)
title: CharField(max_length=200)
description: TextField()
price: DecimalField(max_digits=10, decimal_places=2)
image: ImageField(upload_to='services/events/')
event_type: CharField(max_length=100)
capacity: IntegerField()
duration: IntegerField()
includes_decoration: BooleanField(default=False)
includes_catering: BooleanField(default=False)
created_at: DateTimeField(auto_now_add=True)
updated_at: DateTimeField(auto_now=True)
```

#### Photography
```
pk: integer (primary key)
title: CharField(max_length=200)
description: TextField()
price: DecimalField(max_digits=10, decimal_places=2)
image: ImageField(upload_to='services/photography/')
shoot_type: CharField(max_length=100)
duration: IntegerField()
includes_editing: BooleanField(default=True)
number_of_photos: IntegerField()
includes_prints: BooleanField(default=False)
created_at: DateTimeField(auto_now_add=True)
updated_at: DateTimeField(auto_now=True)
```

#### Catering
```
pk: integer (primary key)
title: CharField(max_length=200)
description: TextField()
price: DecimalField(max_digits=10, decimal_places=2)  # per person
image: ImageField(upload_to='services/catering/')
cuisine_type: CharField(max_length=100)
min_order_quantity: IntegerField()
includes_serving_staff: BooleanField(default=False)
includes_setup: BooleanField(default=False)
created_at: DateTimeField(auto_now_add=True)
updated_at: DateTimeField(auto_now=True)
```

#### PrintingService
```
pk: integer (primary key)
title: CharField(max_length=200)
description: TextField()
price: DecimalField(max_digits=10, decimal_places=2)  # per piece
image: ImageField(upload_to='services/printing/')
print_type: CharField(max_length=100)
paper_type: CharField(max_length=100)
min_order_quantity: IntegerField()
includes_design: BooleanField(default=False)
delivery_time: IntegerField()  # days
created_at: DateTimeField(auto_now_add=True)
updated_at: DateTimeField(auto_now=True)
```

### 2. STORE MODELS

#### StoreCategory
```
pk: integer (primary key)
name: CharField(max_length=100)
description: TextField(blank=True)
```

#### StoreItem
```
pk: integer (primary key)
category: ForeignKey(StoreCategory)
name: CharField(max_length=200)
description: TextField()
price: DecimalField(max_digits=10, decimal_places=2)
image: ImageField(upload_to='store/')
stock: IntegerField(default=0)
created_at: DateTimeField(auto_now_add=True)
updated_at: DateTimeField(auto_now=True)
```

---

## FIXTURE DATA STRUCTURE

### Format
All fixtures follow Django's standard JSON fixture format:

```json
{
  "model": "app_label.model_name",
  "pk": 1,
  "fields": {
    "field_name": "field_value",
    ...
  }
}
```

### Example Entries

#### ServiceCategory
```json
{
  "model": "core.servicecategory",
  "pk": 1,
  "fields": {
    "name": "Event Management",
    "description": "Professional event planning and coordination services"
  }
}
```

#### EventManagement
```json
{
  "model": "core.eventmanagement",
  "pk": 1,
  "fields": {
    "title": "Premium Wedding Coordination Package",
    "description": "Complete wedding planning and coordination...",
    "price": "250000.00",
    "image": "services/wedding_premium_coordination_01.jpg",
    "event_type": "Wedding",
    "capacity": 500,
    "duration": 8,
    "includes_decoration": true,
    "includes_catering": false,
    "created_at": "2025-12-07T10:00:00Z",
    "updated_at": "2025-12-07T10:00:00Z"
  }
}
```

#### Photography
```json
{
  "model": "core.photography",
  "pk": 8,
  "fields": {
    "title": "Wedding Photography - 8 Hours",
    "description": "Comprehensive wedding day photography covering pre-wedding, ceremony, and reception...",
    "price": "45000.00",
    "image": "services/wedding_photography_8hrs_01.jpg",
    "shoot_type": "Wedding",
    "duration": 8,
    "includes_editing": true,
    "number_of_photos": 600,
    "includes_prints": false,
    "created_at": "2025-12-07T10:00:00Z",
    "updated_at": "2025-12-07T10:00:00Z"
  }
}
```

#### Catering
```json
{
  "model": "core.catering",
  "pk": 16,
  "fields": {
    "title": "Premium Bengali Wedding Catering",
    "description": "Authentic Bengali cuisine with 18+ traditional dishes...",
    "price": "850.00",
    "image": "services/bengali_wedding_catering_01.jpg",
    "cuisine_type": "Bengali",
    "min_order_quantity": 50,
    "includes_serving_staff": true,
    "includes_setup": true,
    "created_at": "2025-12-07T10:00:00Z",
    "updated_at": "2025-12-07T10:00:00Z"
  }
}
```

#### PrintingService
```json
{
  "model": "core.printingservice",
  "pk": 24,
  "fields": {
    "title": "Premium Wedding Card Printing",
    "description": "Customized wedding invitation cards on premium cardstock...",
    "price": "50.00",
    "image": "services/premium_wedding_cards_01.jpg",
    "print_type": "Wedding Card",
    "paper_type": "Premium Matte",
    "min_order_quantity": 100,
    "includes_design": true,
    "delivery_time": 7,
    "created_at": "2025-12-07T10:00:00Z",
    "updated_at": "2025-12-07T10:00:00Z"
  }
}
```

#### StoreCategory
```json
{
  "model": "core.storecategory",
  "pk": 1,
  "fields": {
    "name": "Decor Items",
    "description": "Beautiful decorative items for all occasions"
  }
}
```

#### StoreItem
```json
{
  "model": "core.storeitem",
  "pk": 1,
  "fields": {
    "category": 1,
    "name": "Crystal Glass Table Centerpiece with LED Base",
    "description": "Elegant crystal glass centerpiece with rechargeable LED light base...",
    "price": "2500.00",
    "image": "store/crystal_centerpiece_led_01.jpg",
    "stock": 25,
    "created_at": "2025-12-07T10:00:00Z",
    "updated_at": "2025-12-07T10:00:00Z"
  }
}
```

---

## LOADING INSTRUCTIONS

### Command
```bash
cd E:\EvenNest\Main
python manage.py loaddata initial_products.json
```

### Expected Output
```
Installed 59 object(s) from 1 fixture(s)
```

### Verify in Admin
```
http://127.0.0.1:8000/admin/

Admin credentials:
Username: admin
Password: admin123
```

---

## IMAGE FILE NAMING CONVENTION

### Services
Format: `services/[service_type]_[descriptor]_[number].jpg`

Examples:
- `services/wedding_premium_coordination_01.jpg`
- `services/corporate_event_management_01.jpg`
- `services/birthday_photography_01.jpg`
- `services/bengali_wedding_catering_01.jpg`
- `services/premium_wedding_cards_01.jpg`

### Store
Format: `store/[item_type]_[descriptor]_[number].jpg`

Examples:
- `store/crystal_centerpiece_led_01.jpg`
- `store/gold_charger_plates_01.jpg`
- `store/silk_flowers_roses_mix_01.jpg`
- `store/metallic_balloons_100pk_01.jpg`
- `store/led_string_lights_warm_10m_01.jpg`

---

## PRICING GUIDELINES

### Services
- **Event Management**: 35,000 - 350,000 BDT (per event)
- **Photography**: 12,000 - 65,000 BDT (per shoot/package)
- **Catering**: 250 - 850 BDT (per person)
- **Printing**: 3 - 50 BDT (per piece)

### Store Items
- **Decor & Accessories**: 450 - 4,200 BDT
- **Lighting**: 1,200 - 8,500 BDT
- **Floral Items**: 450 - 3,500 BDT

---

## COMMON ISSUES & SOLUTIONS

### Issue: "No such table" error
```
Solution: Run migrations first
python manage.py migrate
```

### Issue: Images not showing
```
Solution 1: Place files in media/ folder with exact filenames
Solution 2: Upload through Django admin interface
Solution 3: Use placeholder images initially
```

### Issue: Duplicate key error
```
Solution: Delete db.sqlite3, run migrate again, then loaddata
```

### Issue: Fixture not found
```
Solution: Ensure file is at core/fixtures/initial_products.json
(not Core/ or other paths)
```

---

## MODIFICATION GUIDE

### To Add New Item:
1. Open `initial_products.json`
2. Find the section for that model (e.g., "model": "core.storeitem")
3. Copy an existing entry
4. Increment the `pk` value to next available number
5. Update all field values
6. Reload: `python manage.py loaddata initial_products.json`

### To Update Existing Item:
1. Edit in Django admin interface (recommended)
2. Or modify JSON and reload fixture
3. Note: Reloading fixture overwrites existing data

### To Add New Category:
1. Add new StoreCategory or ServiceCategory entry
2. Use new pk number
3. Reference in child items with correct category_id
4. Reload fixture

---

## DATA CONSISTENCY CHECKS

✅ All foreign keys point to valid primary keys
✅ All decimal prices have 2 decimal places
✅ All image paths use underscores, no spaces
✅ All descriptions are meaningful and professional
✅ All boolean fields have logical values
✅ All timestamps are ISO format with UTC timezone
✅ No duplicate primary keys
✅ All required fields populated
✅ Stock quantities realistic (0-150 items)
✅ Capacity values logical (50-500+ guests)

---

## BACKUP & RESTORE

### Export Current Data
```bash
python manage.py dumpdata core > backup.json
```

### Restore from Backup
```bash
python manage.py loaddata backup.json
```

### Reset to Seed Data
```bash
# Option 1: Delete db and reload
rm db.sqlite3
python manage.py migrate
python manage.py loaddata initial_products.json

# Option 2: Clear and reload
python manage.py flush
python manage.py loaddata initial_products.json
```

---

## DEPLOYMENT NOTES

- Fixture is designed for development/testing
- Before production, create real vendor accounts
- Update prices and details based on actual business rates
- Set up proper image CDN for production
- Consider splitting fixture into smaller files if database grows
- Archive old fixtures for reference

---

**Document Version**: 1.0  
**Created**: 2025-12-07  
**Compatible**: Django 5.2, Python 3.13, EventNest Project
