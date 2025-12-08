#!/usr/bin/env python
import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Delete existing admin users
User.objects.filter(username='admin').delete()

# Create new superuser
user = User.objects.create_superuser(
    username='admin',
    email='admin@evenest.com',
    password='admin123'
)
print(f'✓ Superuser created successfully')
print(f'Username: admin')
print(f'Password: admin123')
