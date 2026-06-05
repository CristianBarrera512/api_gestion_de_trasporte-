from django.contrib import admin

from django.contrib import admin

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

admin.site.register(Conductores)
admin.site.register(Vehiculo)
admin.site.register(Aseguradora)
admin.site.register(Empresa)
admin.site.register(Documentacion)
admin.site.register(Licencias)
admin.site.register(Rutas)
admin.site.register(Viajes)
admin.site.register(Pasajeros)
admin.site.register(Boletos)
admin.site.register(Estaciones)
admin.site.register(Mantenimiento)
