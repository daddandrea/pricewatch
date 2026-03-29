#!/bin/bash
mkdir -p /app/data
mkdir -p /app/celerybeat
chmod 777 /app/data
chmod 777 /app/celerybeat
python manage.py makemigrations
python manage.py migrate
exec "$@"
