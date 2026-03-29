#!/bin/bash
mkdir -p /app/data
python manage.py makemigrations
python manage.py migrate
exec "$@"
