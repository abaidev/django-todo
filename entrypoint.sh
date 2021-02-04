#!/bin/bash

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# gunicorn for Heroku
echo "Gunicorn starts"
gunicorn server.wsgi:application --bind 0.0.0.0:8000

#echo "DJANGO SERVER starts"
#python3 manage.py runserver 0.0.0.0:8000