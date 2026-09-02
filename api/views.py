from django.shortcuts import render  
from rest_framework import viewsets
from .models import Dueno, Veterinario, Mascota, AtencionMedica
from .serializer import (
    DuenoSerializer, 
    VeterinarioSerializer, 
    MascotaSerializer, 
    AtencionMedicaSerializer
)

# Función para renderizar la página de bienvenida
def bienvenida(request):
    return render(request, 'bienvenida.html')

# ViewSets de la API...
class DuenoViewSet(viewsets.ModelViewSet):
    queryset = Dueno.objects.all()
    serializer_class = DuenoSerializer

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class AtencionMedicaViewSet(viewsets.ModelViewSet):
    queryset = AtencionMedica.objects.all()
    serializer_class = AtencionMedicaSerializer