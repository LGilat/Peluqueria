#!/bin/bash

# Script de inicio para Render (o cualquier otro servicio)
# Este script se ejecuta al iniciar la aplicación.

set -e

# Instalar dependencias (si no están instaladas)
echo "Instalando dependencias..."
pip install -r requirements.txt

# Aplicar migraciones
echo "Aplicando migraciones..."
python manage.py migrate

# Recolectar archivos estáticos
echo "Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

# Iniciar Gunicorn
echo "Iniciando Gunicorn..."
exec gunicorn Peluqueria.wsgi:application --config gunicorn.conf.py
