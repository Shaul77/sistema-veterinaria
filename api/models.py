from django.db import models

class Dueno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr/a. {self.nombre} {self.apellido}"

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad_anos = models.PositiveSmallIntegerField()
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - Dueño: {self.dueno.nombre}"

class AtencionMedica(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_CURSO', 'En Curso'),
        ('FINALIZADA', 'Finalizada'),
        ('CANCELADA', 'Cancelada'),
    ]
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='atenciones')
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='atenciones')
    fecha_atencion = models.DateTimeField(auto_now_add=True)
    motivo_consulta = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')

    def __str__(self):
        return f"Atención #{self.id} - {self.mascota.nombre} ({self.estado})"