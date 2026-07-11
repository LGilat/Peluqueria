# 💇‍♂️ **Sistema de Gestión para Peluquerías**

**API REST para la gestión integral de una peluquería**, construida con **Django** y **Django REST Framework**. Permite gestionar clientes, productos, reservas, facturas, inventario, proveedores y finanzas.

---

## 📌 **Características Principales**

- ✅ **Gestión de Clientes**: Registro y seguimiento de clientes.
- ✅ **Catálogo de Productos**: Productos con imágenes, precios y descripciones.
- ✅ **Control de Inventario**: Gestión de stock por proveedor.
- ✅ **Reservas**: Sistema de citas con estados (pendiente, realizada, cancelada, finalizada).
- ✅ **Facturación**: Generación de facturas con líneas de productos y promociones.
- ✅ **Gestión Financiera**: Registro de ingresos y gastos.
- ✅ **Proveedores**: Base de datos de proveedores.
- ✅ **Promociones**: Descuentos por porcentaje o cantidad fija.
- ✅ **API REST**: Endpoints para todas las entidades.
- ✅ **Listo para Producción**: Configuración para **Render**, **Gunicorn** y **Nginx**.

---

## 🛠 **Tecnologías Utilizadas**

| Tecnología | Versión | Descripción |
|------------|---------|-------------|
| [Python](https://www.python.org/) | 3.13+ | Lenguaje de programación |
| [Django](https://www.djangoproject.com/) | 6.0.7 | Framework web |
| [Django REST Framework](https://www.django-rest-framework.org/) | 3.17.1 | API REST |
| [django-cors-headers](https://github.com/adamchainz/django-cors-headers) | 4.9.0 | Soporte CORS |
| [Pillow](https://python-pillow.org/) | 12.3.0 | Manejo de imágenes |
| [Gunicorn](https://gunicorn.org/) | 22.0.0 | Servidor WSGI para producción |
| [SQLite](https://www.sqlite.org/) | - | Base de datos (desarrollo) |
| [PostgreSQL](https://www.postgresql.org/) | - | Base de datos (producción) |

---

## 🚀 **Instalación y Configuración**

### **1. Requisitos Previos**

- Python 3.13 o superior.
- `pip` (gestor de paquetes de Python).
- Git (opcional, para clonar el repositorio).

### **2. Clonar el Repositorio**

```bash
git clone https://github.com/LGilat/Peluqueria.git
cd Peluqueria
```

### **3. Crear un Entorno Virtual (Recomendado)**

```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### **4. Instalar Dependencias**

```bash
pip install -r requirements.txt
```

### **5. Configurar Variables de Entorno**

Copia el archivo `.env.example` a `.env` y ajusta los valores:

```bash
cp .env.example .env
```

Edita `.env` con tus valores (ejemplo para producción en **Render**):

```env
# Configuración de Django
DJANGO_SECRET_KEY=tu_clave_secreta_segura_y_larga
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=*

# Base de datos (PostgreSQL en Render)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=nombre_de_la_base_de_datos
DB_USER=usuario_de_la_base_de_datos
DB_PASSWORD=contraseña_de_la_base_de_datos
DB_HOST=host_de_la_base_de_datos
DB_PORT=5432

# CORS (opcional)
CORS_ORIGIN_ALLOW_ALL=True
```

> **Nota**: En **Render**, las variables de entorno se configuran en el panel de control del servicio.

### **6. Aplicar Migraciones**

```bash
python manage.py migrate
```

### **7. Crear un Superusuario (Admin)**

```bash
python manage.py createsuperuser
```

### **8. Ejecutar el Servidor de Desarrollo**

```bash
python manage.py runserver
```

> El servidor se iniciará en `http://127.0.0.1:8000/`.

---

## 📡 **Endpoints de la API**

La API está disponible en `/api/` y cuenta con los siguientes endpoints:

| Recurso | Endpoint | Métodos | Descripción |
|---------|----------|---------|-------------|
| **Clientes** | `/api/cliente/` | `GET`, `POST` | Listar y crear clientes |
| | `/api/cliente/<id>/` | `GET`, `PUT`, `DELETE` | Detalles, actualizar y eliminar cliente |
| **Proveedores** | `/api/proveedor/` | `GET`, `POST` | Listar y crear proveedores |
| | `/api/proveedor/<id>/` | `GET`, `PUT`, `DELETE` | Detalles, actualizar y eliminar proveedor |
| **Productos** | `/api/producto/` | `GET`, `POST` | Listar y crear productos |
| | `/api/producto/<id>/` | `GET`, `PUT`, `DELETE` | Detalles, actualizar y eliminar producto |
| **Stock** | `/api/stock/` | `GET`, `POST` | Listar y crear registros de stock |
| | `/api/stock/<id>/` | `GET`, `PUT`, `DELETE` | Detalles, actualizar y eliminar stock |
| **Reservas** | `/api/reserva/` | `GET`, `POST` | Listar y crear reservas |
| | `/api/reserva/<id>/` | `GET`, `PUT`, `DELETE` | Detalles, actualizar y eliminar reserva |
| **Atendentes** | `/api/atendente/` | `GET`, `POST` | Listar y crear atendentes |
| | `/api/atendente/<id>/` | `GET`, `PUT`, `DELETE` | Detalles, actualizar y eliminar atendente |
| **Facturas** | `/api/factura/` | `GET`, `POST` | Listar y crear facturas |
| | `/api/factura/<id>/` | `GET`, `PUT`, `DELETE` | Detalles, actualizar y eliminar factura |
| **Promociones** | `/api/promocion/` | `GET`, `POST` | Listar y crear promociones |
| | `/api/promocion/<id>/` | `GET`, `PUT`, `DELETE` | Detalles, actualizar y eliminar promoción |
| **Ingresos** | `/api/ingreso/` | `GET`, `POST` | Listar y crear ingresos |
| | `/api/ingreso/<id>/` | `GET`, `PUT`, `DELETE` | Detalles, actualizar y eliminar ingreso |
| **Gastos** | `/api/gasto/` | `GET`, `POST` | Listar y crear gastos |
| | `/api/gasto/<id>/` | `GET`, `PUT`, `DELETE` | Detalles, actualizar y eliminar gasto |

---

## 🌐 **Despliegue en Render**

### **1. Preparar el Proyecto**

Asegúrate de que:
- El archivo `requirements.txt` esté actualizado.
- El archivo `render.yaml` esté en la raíz del proyecto.
- Las variables de entorno estén configuradas en el panel de **Render**.

### **2. Configurar el Servicio en Render**

1. **Crear un nuevo servicio Web** en [Render](https://render.com).
2. **Conectar tu repositorio** (GitHub o GitLab).
3. **Configurar el servicio**:
   - **Nombre**: `peluqueria-api` (o el que prefieras).
   - **Región**: `Frankfurt` (o la más cercana a ti).
   - **Rama**: `main` (o la rama que quieras desplegar).
   - **Comando de construcción**:
     ```bash
     pip install -r requirements.txt
     python manage.py migrate
     python manage.py collectstatic --noinput
     ```
   - **Comando de inicio**:
     ```bash
     gunicorn Peluqueria.wsgi:application --bind 0.0.0.0:$PORT
     ```
4. **Configurar variables de entorno** en el panel de Render:
   | Clave | Valor |
   |-------|-------|
   | `DJANGO_SECRET_KEY` | Tu clave secreta (genera una con `python -c "import secrets; print(secrets.token_urlsafe(50))"`) |
   | `DJANGO_DEBUG` | `False` |
   | `DJANGO_ALLOWED_HOSTS` | `*` |
   | `DB_ENGINE` | `django.db.backends.postgresql` |
   | `DB_NAME` | Nombre de tu base de datos en Render |
   | `DB_USER` | Usuario de la base de datos |
   | `DB_PASSWORD` | Contraseña de la base de datos |
   | `DB_HOST` | Host de la base de datos (proporcionado por Render) |
   | `DB_PORT` | `5432` |
   | `CORS_ORIGIN_ALLOW_ALL` | `True` |

5. **Crear la base de datos PostgreSQL** en Render:
   - Ve a **Dashboard > Databases** y crea una nueva base de datos PostgreSQL.
   - Copia los valores de `Database URL` y configúralos en las variables de entorno.

6. **Desplegar el servicio**:
   - Haz clic en **Deploy** y espera a que el proceso termine.

### **3. Configuración Alternativa con `render.yaml`**

Si prefieres usar el archivo `render.yaml`:
1. Asegúrate de que el archivo esté en la raíz del proyecto.
2. Configura las variables de entorno en el panel de Render.
3. Render detectará automáticamente el archivo y desplegará el servicio.

---

## 📂 **Estructura del Proyecto**

```
Peluqueria/
├── Peluqueria/                  # Configuración principal de Django
│   ├── settings.py             # Configuración de la aplicación
│   ├── urls.py                 # Rutas principales
│   ├── wsgi.py                 # Configuración WSGI
│   └── ...
├── gestion_peluqueria/          # App principal
│   ├── models.py               # Modelos de la base de datos
│   ├── views.py                # Vistas (API Views)
│   ├── serializers.py          # Serializadores para DRF
│   ├── urls.py                 # Rutas de la app
│   ├── admin.py                # Configuración del panel de administración
│   └── ...
├── gunicorn.conf.py            # Configuración de Gunicorn
├── start.sh                    # Script de inicio para producción
├── render.yaml                 # Configuración para Render
├── requirements.txt            # Dependencias de Python
├── .env.example                # Ejemplo de variables de entorno
├── .gitignore                  # Archivos ignorados por Git
├── db.sqlite3                  # Base de datos SQLite (desarrollo)
├── manage.py                   # Script de gestión de Django
└── README.md                   # Este archivo
```

---

## 🔧 **Configuración para Producción**

### **1. Base de Datos (PostgreSQL)**

Modifica `settings.py` para usar PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

### **2. Autenticación con JWT**

Instala `djangorestframework-simplejwt`:

```bash
pip install djangorestframework-simplejwt
```

Agrega a `INSTALLED_APPS` en `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
]
```

Configura `REST_FRAMEWORK`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

### **3. Despliegue con Gunicorn + Nginx**

#### **Gunicorn**

El archivo `gunicorn.conf.py` ya está configurado. Puedes ejecutarlo directamente:

```bash
gunicorn Peluqueria.wsgi:application --config gunicorn.conf.py
```

#### **Nginx**

Configura un archivo de configuración para Nginx (`/etc/nginx/sites-available/peluqueria`):

```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias /ruta/a/tu/proyecto/staticfiles/;
    }

    location /media/ {
        alias /ruta/a/tu/proyecto/media/;
    }
}
```

Habilita el sitio y reinicia Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/peluqueria /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

---

## 🧪 **Pruebas**

### **1. Ejecutar Pruebas**

```bash
python manage.py test
```

### **2. Crear Pruebas Personalizadas**

Puedes añadir pruebas en `gestion_peluqueria/tests.py`. Ejemplo:

```python
from django.test import TestCase
from gestion_peluqueria.models import Cliente

class ClienteModelTest(TestCase):
    def test_crear_cliente(self):
        cliente = Cliente.objects.create(
            nombre="Juan",
            apellido="Pérez",
            email="juan@example.com",
            telefono="123456789",
            direccion="Calle Falsa 123"
        )
        self.assertEqual(cliente.nombre, "Juan")
```

---

## 📜 **Licencia**

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo `LICENSE` para más detalles.

---

## 🤝 **Contribuciones**

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un **fork** del repositorio.
2. Crea una **rama** para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz **commit** (`git commit -m "Añade nueva funcionalidad"`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un **Pull Request** en GitHub.

---

## 📞 **Contacto**

Para preguntas o soporte, contacta con el equipo de desarrollo:

- **Email**: [tu-email@example.com](mailto:tu-email@example.com)
- **GitHub**: [@LGilat](https://github.com/LGilat)

---

**© 2025 - Sistema de Gestión para Peluquerías**
