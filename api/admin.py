from django.contrib import admin
from .models import Dueno, Veterinario, Mascota, AtencionMedica

admin.site.register(Dueno)
admin.site.register(Veterinario)
admin.site.register(Mascota)
admin.site.register(AtencionMedica)