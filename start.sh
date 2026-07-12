#!/bin/bash

set -e

python manage.py migrate --noinput
python manage.py create_admin
python manage.py collectstatic --noinput
exec gunicorn Peluqueria.wsgi:application --bind 0.0.0.0:${PORT:-8000}
