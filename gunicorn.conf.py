"""
Configuración de Gunicorn para Django en producción.
Este archivo configura el servidor Gunicorn para servir la aplicación Django.
"""

import multiprocessing
import os

# Direcciones para bind
bind = "0.0.0.0:" + os.getenv("PORT", "8000")

# Número de trabajadores (2 * CPU + 1)
workers = multiprocessing.cpu_count() * 2 + 1

# Tipo de trabajador (recomendado para Django)
worker_class = "gthread"

# Tiempo de espera para trabajadores (segundos)
timeout = 300

# Máximo de solicitudes por trabajador antes de reiniciar
max_requests = 1000
max_requests_jitter = 50

# Nivel de log
loglevel = "info"

# Archivos de log (opcional, descomentar si se necesitan)
# accesslog = "-"
# errorlog = "-"

# Pre-cargar la aplicación para evitar problemas con Django
preload_app = True

# Configuración para entornos con muchas conexiones
keepalive = 5

# Configuración para manejo de señales
graceful_timeout = 30
forwarded_allow_ips = "*"

# Configuración para seguridad
limit_request_fields = 32000
limit_request_field_size = 0  # Sin límite

# Configuración para Django
# Asegúrate de que Django esté configurado para producción
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Peluqueria.settings")
os.environ.setdefault("DJANGO_ENV", "production")
