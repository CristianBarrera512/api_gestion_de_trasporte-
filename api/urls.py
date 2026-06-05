from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import (
    ConductoresViewSet,
    VehiculoViewSet,
    AseguradoraViewSet,
    EmpresaViewSet,
    DocumentacionViewSet,
    LicenciasViewSet,
    RutasViewSet,
    ViajesViewSet,
    PasajerosViewSet,
    BoletosViewSet,
    EstacionesViewSet,
    MantenimientoViewSet
)



router = DefaultRouter()

router.register(r'conductores', ConductoresViewSet, basename='conductores')
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculos')
router.register(r'aseguradoras', AseguradoraViewSet, basename='aseguradoras')
router.register(r'empresas', EmpresaViewSet, basename='empresas')
router.register(r'documentaciones', DocumentacionViewSet, basename='documentaciones')
router.register(r'licencias', LicenciasViewSet, basename='licencias')
router.register(r'rutas', RutasViewSet, basename='rutas')
router.register(r'viajes', ViajesViewSet, basename='viajes')
router.register(r'pasajeros', PasajerosViewSet, basename='pasajeros')
router.register(r'boletos', BoletosViewSet, basename='boletos')
router.register(r'estaciones', EstacionesViewSet, basename='estaciones')
router.register(r'mantenimientos', MantenimientoViewSet, basename='mantenimientos')

urlpatterns = router.urls + [
    path(
        'auth/login/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'auth/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]