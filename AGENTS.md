# Comandos para el Proyecto Peluquería

## Entorno Virtual
```bash
source /home/debianlg/programacion/python/pyvenv/bin/activate
```

## Verificación y Pruebas
```bash
# Verificar configuración Django
python manage.py check

# Ejecutar pruebas
python manage.py test

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate
```

## Linting (si se instala flake8 o similar)
```bash
# Instalar flake8 (opcional)
pip install flake8

# Ejecutar linting
flake8 gestion_peluqueria/
```

## Ejecutar Servidor
```bash
python manage.py runserver
```

## API Endpoints
- `GET /api/` - Información de la API
- `POST /api/token/` - Autenticación JWT (obtener token)
- `POST /api/token/refresh/` - Renovar token JWT
- `GET/POST /api/cliente/` - Gestión de clientes
- `GET/POST /api/proveedor/` - Gestión de proveedores
- `GET/POST /api/producto/` - Gestión de productos
- `GET/POST /api/stock/` - Gestión de inventario
- `GET/POST /api/atendente/` - Gestión de atendentes
- `GET/POST /api/reserva/` - Gestión de reservas
- `GET/POST /api/factura/` - Gestión de facturas
- `GET/POST /api/ingreso/` - Gestión de ingresos
- `GET/POST /api/gasto/` - Gestión de gastos
- `GET/POST /api/promocion/` - Gestión de promociones

## Notas
- El proyecto utiliza SQLite para desarrollo
- CORS está configurado para localhost:5173
- API REST expuesta en /api/
- Autenticación JWT implementada con djangorestframework-simplejwt
- Validaciones de negocio añadidas a reservas (fecha no pasada, disponibilidad de horario)
- Configuración para PostgreSQL añadida (comentada) para producción