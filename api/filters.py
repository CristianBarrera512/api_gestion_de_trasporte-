import django_filters

from .models import (
    Vehiculo,
    Aseguradora,
    Empresa,
    Documentacion,
    Licencias,
    Conductores,
    Rutas,
    Viajes,
    Pasajeros,
    Boletos,
    Estaciones,
    Mantenimiento,
)


class VehiculoFilter(django_filters.FilterSet):
    placa = django_filters.CharFilter(lookup_expr='icontains')
    modelo = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Vehiculo
        fields = ['placa', 'modelo', 'activo']


class AseguradoraFilter(django_filters.FilterSet):
    nombre_aseguradora = django_filters.CharFilter(lookup_expr='icontains')
    telefono = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Aseguradora
        fields = ['nombre_aseguradora', 'telefono', 'activo']


class EmpresaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    direccion = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Empresa
        fields = ['nombre', 'direccion', 'activo']


class DocumentacionFilter(django_filters.FilterSet):
    tipo_documento = django_filters.CharFilter(lookup_expr='icontains')
    numero_documento = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Documentacion
        fields = ['tipo_documento', 'numero_documento', 'activo']


class LicenciasFilter(django_filters.FilterSet):
    numero_licencia = django_filters.CharFilter(lookup_expr='icontains')
    categoria = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Licencias
        fields = ['numero_licencia', 'categoria', 'activo']


class ConductoresFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    edad = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Conductores
        fields = [
            'nombre',
            'edad',
            'activo',
            'id_empresa',
            'id_aseguradora',
            'id_licencia'
        ]


class RutasFilter(django_filters.FilterSet):
    nombre_ruta = django_filters.CharFilter(lookup_expr='icontains')
    lugar_salida = django_filters.CharFilter(lookup_expr='icontains')
    lugar_llega = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Rutas
        fields = [
            'nombre_ruta',
            'lugar_salida',
            'lugar_llega',
            'activo'
        ]


class ViajesFilter(django_filters.FilterSet):
    fecha_viaje = django_filters.DateFilter()
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Viajes
        fields = [
            'fecha_viaje',
            'activo',
            'id_ruta'
        ]


class PasajerosFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Pasajeros
        fields = [
            'nombre',
            'activo',
            'id_documento'
        ]


class BoletosFilter(django_filters.FilterSet):
    estado = django_filters.CharFilter(lookup_expr='icontains')
    precio = django_filters.NumberFilter()
    
    class Meta:
        model = Boletos
        fields = [
            'estado',
            'precio',
            'id_pasajero',
            'id_viaje'
        ]


class EstacionesFilter(django_filters.FilterSet):
    nombre_estacion = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Estaciones
        fields = [
            'nombre_estacion',
            'activo',
            'id_rutas'
        ]


class MantenimientoFilter(django_filters.FilterSet):
    clase_matenimiento = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()

    class Meta:
        model = Mantenimiento
        fields = [
            'clase_matenimiento',
            'activo',
            'id_vehiculo'
        ]


