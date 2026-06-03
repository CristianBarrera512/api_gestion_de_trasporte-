
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from .models import (
    Conductores,
    Vehiculo,
    Aseguradora,
    Empresa,
    Documentacion,
    Licencias,
    Rutas,
    Viajes,
    Pasajeros,
    Boletos,
    Estaciones,
    Mantenimiento,
)

from .serializers import (
    ConductoresSerializer,
    VehiculoSerializer,
    AseguradoraSerializer,
    EmpresaSerializer,
    DocumentacionSerializer,
    LicenciasSerializer,
    RutasSerializer,
    ViajesSerializer,
    PasajerosSerializer,
    BoletosSerializer,
    EstacionesSerializer,
    MantenimientoSerializer
)


class ConductoresViewSet(viewsets.ModelViewSet):
    queryset = Conductores.objects.all()
    serializer_class = ConductoresSerializer

    @swagger_auto_schema(operation_description="Lista de conductores")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

    @swagger_auto_schema(operation_description="Lista de vehículos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AseguradoraViewSet(viewsets.ModelViewSet):
    queryset = Aseguradora.objects.all()
    serializer_class = AseguradoraSerializer

    @swagger_auto_schema(operation_description="Lista de aseguradoras")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    @swagger_auto_schema(operation_description="Lista de empresas")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DocumentacionViewSet(viewsets.ModelViewSet):
    queryset = Documentacion.objects.all()
    serializer_class = DocumentacionSerializer

    @swagger_auto_schema(operation_description="Lista de documentos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class LicenciasViewSet(viewsets.ModelViewSet):
    queryset = Licencias.objects.all()
    serializer_class = LicenciasSerializer

    @swagger_auto_schema(operation_description="Lista de licencias")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RutasViewSet(viewsets.ModelViewSet):
    queryset = Rutas.objects.all()
    serializer_class = RutasSerializer

    @swagger_auto_schema(operation_description="Lista de rutas")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ViajesViewSet(viewsets.ModelViewSet):
    queryset = Viajes.objects.all()
    serializer_class = ViajesSerializer

    @swagger_auto_schema(operation_description="Lista de viajes")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PasajerosViewSet(viewsets.ModelViewSet):
    queryset = Pasajeros.objects.all()
    serializer_class = PasajerosSerializer

    @swagger_auto_schema(operation_description="Lista de pasajeros")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BoletosViewSet(viewsets.ModelViewSet):
    queryset = Boletos.objects.all()
    serializer_class = BoletosSerializer

    @swagger_auto_schema(operation_description="Lista de boletos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class EstacionesViewSet(viewsets.ModelViewSet):
    queryset = Estaciones.objects.all()
    serializer_class = EstacionesSerializer

    @swagger_auto_schema(operation_description="Lista de estaciones")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer

    @swagger_auto_schema(operation_description="Lista de mantenimientos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)