from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Cliente, Proveedor, Producto, Atendente, Reserva
from .serializers import ClienteSerializer, ProveedorSerializer, ProductoSerializer


class ClienteModelTest(TestCase):
    """Pruebas para el modelo Cliente."""

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Juan",
            apellido="Pérez",
            email="juan@example.com",
            telefono="123456789",
            direccion="Calle Falsa 123"
        )

    def test_crear_cliente(self):
        """Prueba que un cliente se crea correctamente."""
        self.assertEqual(self.cliente.nombre, "Juan")
        self.assertEqual(self.cliente.apellido, "Pérez")
        self.assertEqual(self.cliente.email, "juan@example.com")

    def test_str_cliente(self):
        """Prueba el método __str__ de Cliente."""
        self.assertEqual(str(self.cliente), "Juan Pérez")


class ProveedorModelTest(TestCase):
    """Pruebas para el modelo Proveedor."""

    def setUp(self):
        self.proveedor = Proveedor.objects.create(
            nombre="Proveedor SA",
            email="contacto@proveedor.com",
            telefono="987654321",
            direccion="Avenida Principal 456"
        )

    def test_crear_proveedor(self):
        """Prueba que un proveedor se crea correctamente."""
        self.assertEqual(self.proveedor.nombre, "Proveedor SA")
        self.assertEqual(self.proveedor.email, "contacto@proveedor.com")

    def test_str_proveedor(self):
        """Prueba el método __str__ de Proveedor."""
        self.assertEqual(str(self.proveedor), "Proveedor SA")


class ProductoModelTest(TestCase):
    """Pruebas para el modelo Producto."""

    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Champú Anticaspa",
            descripcion="Champú para eliminar la caspa",
            precio=15.99
        )

    def test_crear_producto(self):
        """Prueba que un producto se crea correctamente."""
        self.assertEqual(self.producto.nombre, "Champú Anticaspa")
        self.assertEqual(self.producto.precio, 15.99)

    def test_str_producto(self):
        """Prueba el método __str__ de Producto."""
        self.assertEqual(str(self.producto), "Champú Anticaspa")


class AtendenteModelTest(TestCase):
    """Pruebas para el modelo Atendente."""

    def setUp(self):
        self.atendente = Atendente.objects.create(
            nombre="Ana",
            apellido="Gómez",
            email="ana@peluqueria.com",
            telefono="555123456",
            especialidad="Cortes de cabello",
            contacto="555123456"
        )

    def test_crear_atendente(self):
        """Prueba que un atendente se crea correctamente."""
        self.assertEqual(self.atendente.nombre, "Ana")
        self.assertEqual(self.atendente.especialidad, "Cortes de cabello")

    def test_str_atendente(self):
        """Prueba el método __str__ de Atendente."""
        self.assertEqual(str(self.atendente), "Ana Gómez")


class ReservaModelTest(TestCase):
    """Pruebas para el modelo Reserva."""

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="María",
            apellido="López",
            email="maria@example.com",
            telefono="111222333",
            direccion="Calle Real 789"
        )
        self.atendente = Atendente.objects.create(
            nombre="Carlos",
            apellido="Martínez",
            email="carlos@peluqueria.com",
            telefono="444555666",
            especialidad="Coloración",
            contacto="444555666"
        )
        self.reserva = Reserva.objects.create(
            cliente=self.cliente,
            servicio="Corte y coloración",
            fecha="2025-12-25",
            hora="10:00:00",
            estado="pendiente",
            atendente=self.atendente
        )

    def test_crear_reserva(self):
        """Prueba que una reserva se crea correctamente."""
        self.assertEqual(self.reserva.servicio, "Corte y coloración")
        self.assertEqual(self.reserva.estado, "pendiente")
        self.assertEqual(self.reserva.cliente, self.cliente)

    def test_str_reserva(self):
        """Prueba el método __str__ de Reserva."""
        self.assertEqual(str(self.reserva), f"Reserva #{self.reserva.id} para María - Servicio: Corte y coloración")


class ClienteAPITest(TestCase):
    """Pruebas para la API de Clientes."""

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('cliente-list')
        self.cliente_data = {
            'nombre': 'Pedro',
            'apellido': 'Sánchez',
            'email': 'pedro@example.com',
            'telefono': '777888999',
            'direccion': 'Calle Nueva 101'
        }

    def test_listar_clientes(self):
        """Prueba que se pueden listar clientes."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_cliente(self):
        """Prueba que se puede crear un cliente."""
        response = self.client.post(self.url, self.cliente_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Cliente.objects.get().nombre, 'Pedro')


class ProveedorAPITest(TestCase):
    """Pruebas para la API de Proveedores."""

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('proveedor-list')
        self.proveedor_data = {
            'nombre': 'Distribuidora XYZ',
            'email': 'ventas@xyz.com',
            'telefono': '123123123',
            'direccion': 'Polígono Industrial 1'
        }

    def test_listar_proveedores(self):
        """Prueba que se pueden listar proveedores."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_proveedor(self):
        """Prueba que se puede crear un proveedor."""
        response = self.client.post(self.url, self.proveedor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Proveedor.objects.count(), 1)


class ProductoAPITest(TestCase):
    """Pruebas para la API de Productos."""

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('producto-list')
        self.producto_data = {
            'nombre': 'Acondicionador',
            'descripcion': 'Acondicionador para cabello seco',
            'precio': 12.50
        }

    def test_listar_productos(self):
        """Prueba que se pueden listar productos."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_producto(self):
        """Prueba que se puede crear un producto."""
        response = self.client.post(self.url, self.producto_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.count(), 1)
