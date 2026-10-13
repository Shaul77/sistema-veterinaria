from django.urls import path, include
from rest_framework import routers
from django.contrib.auth import views as auth_views
from . import views

# Router para la API REST (DRF)
router = routers.DefaultRouter()
router.register(r'duenos', views.DuenoViewSet)
router.register(r'veterinarios', views.VeterinarioViewSet)
router.register(r'mascotas', views.MascotaViewSet)
router.register(r'atenciones', views.AtencionMedicaViewSet)

urlpatterns = [
    # Vista publica de bienvenida
    path('', views.bienvenida, name='bienvenida'),

    # Autenticacion
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Vista protegida basada en funcion (FBV)
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Vista protegida basada en clase (CBV)
    path('reporte/', views.ReporteAtencionesView.as_view(), name='reporte'),

    # Endpoints de la API RESTful
    path('api/', include(router.urls)),
]