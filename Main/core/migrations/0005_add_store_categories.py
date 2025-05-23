# Generated by Django 5.2 on 2025-05-04 19:10

from django.db import migrations

def add_store_categories(apps, schema_editor):
    StoreCategory = apps.get_model('core', 'StoreCategory')
    categories = [
        {
            'name': 'Decor Items',
            'description': 'Beautiful decorative items for all occasions'
        },
        {
            'name': 'Event Accessories',
            'description': 'Essential accessories for event planning and decoration'
        }
    ]
    
    for category_data in categories:
        StoreCategory.objects.get_or_create(
            name=category_data['name'],
            defaults={'description': category_data['description']}
        )

def remove_store_categories(apps, schema_editor):
    StoreCategory = apps.get_model('core', 'StoreCategory')
    StoreCategory.objects.filter(name__in=['Decor Items', 'Event Accessories']).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_catering_eventmanagement_photography_printingservice'),
    ]

    operations = [
        migrations.RunPython(add_store_categories, remove_store_categories),
    ]
