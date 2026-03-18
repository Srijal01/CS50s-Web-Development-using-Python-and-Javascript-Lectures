import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser 'admin' created with password 'admin123'")
else:
    print("Superuser 'admin' already exists")

# Create some regular users
users_data = [
    ('alice', 'alice@example.com', 'Alice', 'Smith'),
    ('bob', 'bob@example.com', 'Bob', 'Johnson'),
]

for username, email, first_name, last_name in users_data:
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username, email, 'password123')
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        print(f"User '{username}' created with password 'password123'")
    else:
        print(f"User '{username}' already exists")

print("\nYou can now log in at:")
print("- Admin: http://localhost:8000/admin/")
print("- Users: http://localhost:8000/users/")
print("- Flights: http://localhost:8000/flights/")
