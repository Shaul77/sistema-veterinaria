"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views  # <-- Importamos las vistas de la app 'api'

urlpatterns = [
    path('admin/', admin.site.urls),  #[cite: 2]
    path('api/', include('api.urls')),  #[cite: 2]
    path('', views.bienvenida, name='bienvenida'),  # <-- Ruta raíz para la bienvenida
]

