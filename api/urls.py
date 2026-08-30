from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'duenos', views.DuenoViewSet)
router.register(r'veterinarios', views.VeterinarioViewSet)
router.register(r'mascotas', views.MascotaViewSet)
router.register(r'atenciones', views.AtencionMedicaViewSet)

urlpatterns = [
    path('', include(router.urls))
]