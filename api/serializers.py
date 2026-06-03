from rest_framework import serializers

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


class ConductoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductores
        fields = '__all__'


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class AseguradoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aseguradora
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class DocumentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentacion
        fields = '__all__'


class LicenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licencias
        fields = '__all__'


class RutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutas
        fields = '__all__'


class ViajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viajes
        fields = '__all__'


class PasajerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajeros
        fields = '__all__'


class BoletosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boletos
        fields = '__all__'


class EstacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estaciones
        fields = '__all__'


class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'