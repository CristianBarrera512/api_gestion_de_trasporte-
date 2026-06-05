from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
import logging

from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.http import HttpResponse
from openpyxl import Workbook

from .base_viewset import BaseViewSet
from .permissions import SoloAdminElimina

logger = logging.getLogger('api.views')

from .filters import *
from .models import *
from .serializers import *




class ConductoresViewSet(BaseViewSet):
    queryset = Conductores.objects.all()
    serializer_class = ConductoresSerializer
    permission_classes = [SoloAdminElimina]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ConductoresFilter

    ordering_fields = '__all__'
    ordering = ['nombre']

    @swagger_auto_schema(operation_description="Lista de conductores")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(
            f'CREAR | Conductor id={instance.pk} nombre={instance.nombre}'
        )

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(
            f'MODIFICAR | Conductor id={instance.pk} nombre={instance.nombre}'
        )

    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )


class VehiculoViewSet(BaseViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = VehiculoFilter

    ordering_fields = ['placa', 'modelo']
    ordering = ['placa']

    @swagger_auto_schema(operation_description="Lista de vehiculos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(
            f'CREAR | Vehiculo id={instance.pk} placa={instance.placa}'
        )

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(
            f'MODIFICAR | Vehiculo id={instance.pk} placa={instance.placa}'
        )


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )


class AseguradoraViewSet(BaseViewSet):
    queryset = Aseguradora.objects.all()
    serializer_class = AseguradoraSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AseguradoraFilter

    ordering_fields = ['nombre_aseguradora', 'telefono']
    ordering = ['nombre_aseguradora']


    @swagger_auto_schema(operation_description="Lista de aseguradoras")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(
            f'CREAR | Aseguradora id={instance.pk} nombre_aseguradora={instance.nombre_aseguradora}'
        )

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(
            f'MODIFICAR | Aseguradora id={instance.pk} nombre_aseguradora={instance.nombre_aseguradora}'
        )


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )



class EmpresaViewSet(BaseViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EmpresaFilter

    ordering_fields = ['nombre', 'direccion']
    ordering = ['nombre']

    @swagger_auto_schema(operation_description="Lista de empresas")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f'CREAR | Empresa id={instance.pk} nombre={instance.nombre}')

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f'MODIFICAR | Empresa id={instance.pk} nombre={instance.nombre}')


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )


class DocumentacionViewSet(BaseViewSet):
    queryset = Documentacion.objects.all()
    serializer_class = DocumentacionSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = DocumentacionFilter

    ordering_fields = ['tipo_documento', 'numero_documento']
    ordering = ['tipo_documento']

    @swagger_auto_schema(operation_description="Lista de documentos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f'CREAR | Documento id={instance.pk}')

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f'MODIFICAR | Documento id={instance.pk}')


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )

class LicenciasViewSet(BaseViewSet):
    queryset = Licencias.objects.all()
    serializer_class = LicenciasSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = LicenciasFilter

    ordering_fields = ['numero_licencia', 'categoria', 'fecha_vencimiento']
    ordering = ['numero_licencia']

    @swagger_auto_schema(operation_description="Lista de licencias")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f'CREAR | Licencia id={instance.pk}')

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f'MODIFICAR | Licencia id={instance.pk}')


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )


class RutasViewSet(BaseViewSet):
    queryset = Rutas.objects.all()
    serializer_class = RutasSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = RutasFilter

    ordering_fields = ['nombre_ruta', 'lugar_salida', 'lugar_llega']
    ordering = ['nombre_ruta']
    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(
            f'CREAR | Ruta id={instance.pk} nombre={instance.nombre_ruta}'
        )

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(
            f'MODIFICAR | Ruta id={instance.pk} nombre={instance.nombre_ruta}'
        )


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )


class ViajesViewSet(BaseViewSet):
    queryset = Viajes.objects.all()
    serializer_class = ViajesSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ViajesFilter

    ordering_fields = ['fecha_viaje', 'hora_salida', 'hora_llegada']
    ordering = ['fecha_viaje']

    @swagger_auto_schema(operation_description="Lista de viajes")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f'CREAR | Viaje id={instance.pk}')

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f'MODIFICAR | Viaje id={instance.pk}')


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )



class PasajerosViewSet(BaseViewSet):
    queryset = Pasajeros.objects.all()
    serializer_class = PasajerosSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PasajerosFilter

    ordering_fields = ['nombre']
    ordering = ['nombre']

    @swagger_auto_schema(operation_description="Lista de pasajeros")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f'CREAR | Pasajero id={instance.pk} nombre={instance.nombre}')

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f'MODIFICAR | Pasajero id={instance.pk} nombre={instance.nombre}')


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )


class BoletosViewSet(BaseViewSet):
    queryset = Boletos.objects.all()
    serializer_class = BoletosSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = BoletosFilter

    ordering_fields = ['numero_asiento', 'precio', 'estado']
    ordering = ['numero_asiento']

    @swagger_auto_schema(operation_description="Lista de boletos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f'CREAR | Boleto id={instance.pk}')

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f'MODIFICAR | Boleto id={instance.pk}')


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )



class EstacionesViewSet(BaseViewSet):
    queryset = Estaciones.objects.all()
    serializer_class = EstacionesSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EstacionesFilter

    ordering_fields = ['nombre_estacion']
    ordering = ['nombre_estacion']

    @swagger_auto_schema(operation_description="Lista de estaciones")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f'CREAR | Estacion id={instance.pk}')

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f'MODIFICAR | Estacion id={instance.pk}')


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )



class MantenimientoViewSet(BaseViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer
    permission_classes = [SoloAdminElimina]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MantenimientoFilter

    ordering_fields = ['clase_matenimiento']
    ordering = ['clase_matenimiento']

    @swagger_auto_schema(operation_description="Lista de mantenimientos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f'CREAR | Mantenimiento id={instance.pk}')

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f'MODIFICAR | Mantenimiento id={instance.pk}')


    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

        logger.info(
        f'ELIMINAR (LOGICO) | Conductor id={instance.pk} nombre={instance.nombre}'
        )



