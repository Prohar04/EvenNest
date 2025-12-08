from django.contrib.auth.models import User
User.objects.filter(username='admin').delete()
user = User.objects.create_superuser('admin', 'admin@evenest.com', 'admin123')
print('Superuser created successfully!')
print('Username: admin')
print('Password: admin123')
