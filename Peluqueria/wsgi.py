"""
WSGI config for Peluqueria project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Peluqueria.settings')

# Configurar el entorno para producción
os.environ.setdefault('DJANGO_ENV', 'production')

# Aplicación WSGI
application = get_wsgi_application()

# Configuración para Whitenoise (servir archivos estáticos en producción)
# Descomentar si se usa Whitenoise
# from whitenoise import WhiteNoise
# application = WhiteNoise(application)
