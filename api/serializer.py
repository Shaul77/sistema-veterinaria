from rest_framework import serializers
from .models import Dueno, Veterinario, Mascota, AtencionMedica

class DuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueno
        fields = '__all__'

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class AtencionMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtencionMedica
        fields = '__all__'