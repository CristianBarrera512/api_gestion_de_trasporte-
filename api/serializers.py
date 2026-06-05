from rest_framework import serializers
from django.contrib.auth import authenticate
from .audit import AuditMixin
from .models import *

class VehiculoSerializer(AuditMixin, serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class AseguradoraSerializer(AuditMixin, serializers.ModelSerializer):
    class Meta:
        model = Aseguradora
        fields = '__all__'


class EmpresaSerializer(AuditMixin, serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class DocumentacionSerializer(AuditMixin, serializers.ModelSerializer):
    class Meta:
        model = Documentacion
        fields = '__all__'


class LicenciasSerializer(AuditMixin, serializers.ModelSerializer):
    class Meta:
        model = Licencias
        fields = '__all__'


class RutasSerializer(AuditMixin, serializers.ModelSerializer):
    class Meta:
        model = Rutas
        fields = '__all__'


class PasajerosSerializer(AuditMixin, serializers.ModelSerializer):

    documento_info = DocumentacionSerializer(source='id_documento', read_only=True)

    id_documento = serializers.PrimaryKeyRelatedField(
        queryset=Documentacion.objects.all()
    )

    class Meta:
        model = Pasajeros
        fields = '__all__'

class ViajesSerializer(AuditMixin, serializers.ModelSerializer):
    class Meta:
        model = Viajes
        fields = '__all__'


class EstacionesSerializer(AuditMixin, serializers.ModelSerializer):
    class Meta:
        model = Estaciones
        fields = '__all__'


class MantenimientoSerializer(AuditMixin, serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'

class ConductoresSerializer(AuditMixin, serializers.ModelSerializer):

    aseguradora_info = AseguradoraSerializer(source='id_aseguradora', read_only=True)
    empresa_info = EmpresaSerializer(source='id_empresa', read_only=True)
    documento_info = DocumentacionSerializer(source='id_documento', read_only=True)
    licencia_info = LicenciasSerializer(source='id_licencia', read_only=True)
    id_aseguradora = serializers.PrimaryKeyRelatedField(queryset=Aseguradora.objects.all())
    id_empresa = serializers.PrimaryKeyRelatedField(queryset=Empresa.objects.all())
    id_documento = serializers.PrimaryKeyRelatedField(queryset=Documentacion.objects.all())
    id_licencia = serializers.PrimaryKeyRelatedField(queryset=Licencias.objects.all())

    class Meta:
        model = Conductores
        fields = '__all__'

class ViajesSerializer(AuditMixin, serializers.ModelSerializer):

    ruta_info = RutasSerializer(source='id_ruta', read_only=True)

    id_ruta = serializers.PrimaryKeyRelatedField(queryset=Rutas.objects.all())

    class Meta:
        model = Viajes
        fields = '__all__'

class BoletosSerializer(AuditMixin, serializers.ModelSerializer):

    # 👀 lectura completa (JOIN visual)
    pasajero_info = PasajerosSerializer(source='id_pasajero', read_only=True)
    viaje_info = ViajesSerializer(source='id_viaje', read_only=True)

    # ✍️ escritura por ID
    id_pasajero = serializers.PrimaryKeyRelatedField(queryset=Pasajeros.objects.all())
    id_viaje = serializers.PrimaryKeyRelatedField(queryset=Viajes.objects.all())

    class Meta:
        model = Boletos
        fields = '__all__'


class EstacionesSerializer(AuditMixin, serializers.ModelSerializer):

    ruta_info = RutasSerializer(source='id_rutas', read_only=True)
    id_rutas = serializers.PrimaryKeyRelatedField(queryset=Rutas.objects.all())

    class Meta:
        model = Estaciones
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def valiate(self, data):
        user =authenticate(    
            username = data.get('username'),
            password = data.get('password')
        )
        if user is not None:
            return user
        raise serializers.ValidationError('usuario o contraseña incorrectos')
    

