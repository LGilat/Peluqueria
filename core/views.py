from rest_framework.views import APIView
from rest_framework.response import Response


class ApiInfoView(APIView):
    """
    Vista para obtener información sobre la API.
    """
    permission_classes = []  # Sin autenticación requerida

    def get(self, request):
        info = {
            "name": "Peluquería API",
            "version": "1.0.0",
            "description": "API REST para gestión de peluquería",
            "endpoints": {
                "auth": {
                    "token": "/api/token/",
                    "refresh": "/api/token/refresh/"
                },
                "resources": {
                    "cliente": "/api/cliente/",
                    "proveedor": "/api/proveedor/",
                    "producto": "/api/producto/",
                    "stock": "/api/stock/",
                    "atendente": "/api/atendente/",
                    "reserva": "/api/reserva/",
                    "historial-reserva": "/api/historial-reserva/",
                    "factura": "/api/factura/",
                    "linea-factura": "/api/linea-factura/",
                    "ingreso": "/api/ingreso/",
                    "gasto": "/api/gasto/",
                    "promocion": "/api/promocion/",
                }
            }
        }
        return Response(info)
