from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework import viewsets
from .models import Dueno, Veterinario, Mascota, AtencionMedica
from .serializer import (
    DuenoSerializer,
    VeterinarioSerializer,
    MascotaSerializer,
    AtencionMedicaSerializer
)

# Vista para la pagina principal de bienvenida
def bienvenida(request):
    # Diccionario con datos del sistema para pasar a la plantilla HTML
    contexto = {
        'titulo': 'Sistema de Gestion Veterinaria',
        'descripcion': 'Plataforma para administrar pacientes, duenos y atenciones medicas.',
        'servicios': [
            'Consultas medicas generales',
            'Vacunacion y desparasitacion',
            'Cirugias y urgencias',
            'Control de fichas clinicas'
        ],
        'estado_sistema': 'Operativo'
    }
    return render(request, 'bienvenida.html', contexto)

# Vista personalizada para manejar el error 404 (pagina no encontrada)
def pagina_no_encontrada(request, exception=None):
    return render(request, '404.html', status=404)

# Vista protegida basada en funcion
@login_required
def dashboard_view(request):
    contexto = {
        'total_duenos': Dueno.objects.count(),
        'total_mascotas': Mascota.objects.count(),
        'total_veterinarios': Veterinario.objects.count(),
        'total_atenciones': AtencionMedica.objects.count(),
        'usuario': request.user,
    }
    return render(request, 'dashboard.html', contexto)

# Vista protegida basada en clase
class ReporteAtencionesView(LoginRequiredMixin, TemplateView):
    template_name = 'reporte.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atenciones'] = AtencionMedica.objects.select_related('mascota', 'veterinario').all()[:10]
        context['usuario'] = self.request.user
        return context

# Vistas de la API para gestionar los duenos de mascotas
class DuenoViewSet(viewsets.ModelViewSet):
    queryset = Dueno.objects.all()
    serializer_class = DuenoSerializer

# Vistas de la API para gestionar los veterinarios
class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer

# Vistas de la API para gestionar las mascotas
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

# Vistas de la API para gestionar las atenciones medicas
class AtencionMedicaViewSet(viewsets.ModelViewSet):
    queryset = AtencionMedica.objects.all()
    serializer_class = AtencionMedicaSerializer