#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.filter(username='admin').first()
if user:
    user.set_password('admin123')
    user.is_staff = True
    user.is_superuser = True
    user.save()
else:
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
"

