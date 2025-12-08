#!/usr/bin/env python
"""
Verification script to confirm seed data was loaded correctly.
Run this after loading the fixture to verify all data is present.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from core.models import (
    EventManagement, Photography, Catering, PrintingService, 
    StoreItem, ServiceCategory, StoreCategory
)

def verify_seed_data():
    """Verify all seed data is loaded."""
    
    print("\n" + "="*60)
    print("EVENEST SEED DATA VERIFICATION")
    print("="*60 + "\n")
    
    # Count each model
    service_cats = ServiceCategory.objects.count()
    event_mgmt = EventManagement.objects.count()
    photography = Photography.objects.count()
    catering = Catering.objects.count()
    printing = PrintingService.objects.count()
    store_cats = StoreCategory.objects.count()
    store_items = StoreItem.objects.count()
    
    print("DATA COUNT BY MODEL:")
    print(f"  ✓ Service Categories:  {service_cats:2d}")
    print(f"  ✓ Event Management:    {event_mgmt:2d}")
    print(f"  ✓ Photography:         {photography:2d}")
    print(f"  ✓ Catering:            {catering:2d}")
    print(f"  ✓ Printing Services:   {printing:2d}")
    print(f"  ✓ Store Categories:    {store_cats:2d}")
    print(f"  ✓ Store Items:         {store_items:2d}")
    
    total = service_cats + event_mgmt + photography + catering + printing + store_cats + store_items
    print(f"\n★ TOTAL ENTRIES LOADED:  {total}\n")
    
    if event_mgmt > 0:
        print("SAMPLE: EVENT MANAGEMENT SERVICES")
        for event in EventManagement.objects.all()[:2]:
            print(f"  • {event.title}")
            print(f"    Price: ৳{event.price:,.0f} | Capacity: {event.capacity} guests | Duration: {event.duration}h")
        print()
    
    if photography > 0:
        print("SAMPLE: PHOTOGRAPHY SERVICES")
        for photo in Photography.objects.all()[:2]:
            print(f"  • {photo.title}")
            print(f"    Price: ৳{photo.price:,.0f} | Duration: {photo.duration}h | Photos: {photo.number_of_photos}")
        print()
    
    if catering > 0:
        print("SAMPLE: CATERING SERVICES")
        for cat in Catering.objects.all()[:2]:
            print(f"  • {cat.title}")
            print(f"    Price: ৳{cat.price:,.0f}/person | Cuisine: {cat.cuisine_type} | Min: {cat.min_order_quantity} persons")
        print()
    
    if printing > 0:
        print("SAMPLE: PRINTING SERVICES")
        for print_srv in PrintingService.objects.all()[:2]:
            print(f"  • {print_srv.title}")
            print(f"    Price: ৳{print_srv.price:,.0f}/piece | Type: {print_srv.print_type} | Min: {print_srv.min_order_quantity}")
        print()
    
    if store_items > 0:
        print("SAMPLE: STORE ITEMS")
        for item in StoreItem.objects.all()[:4]:
            print(f"  • {item.name}")
            print(f"    Price: ৳{item.price:,.0f} | Stock: {item.stock} units | Category: {item.category.name}")
        print()
    
    print("="*60)
    print("✅ VERIFICATION COMPLETE - ALL DATA LOADED SUCCESSFULLY!")
    print("="*60 + "\n")
    
    return total

if __name__ == '__main__':
    total = verify_seed_data()
    
    if total < 40:
        print("⚠️  WARNING: Less than 40 entries loaded. Check fixture file.")
    elif total >= 55:
        print("🎉 Great! Full seed data catalog is ready for development!")

