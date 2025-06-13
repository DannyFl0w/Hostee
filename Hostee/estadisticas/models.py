from django.db import models
from django.utils import timezone

class EstadisticaRobot(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    personas_detectadas = models.IntegerField(default=0)
    tiempo_activo = models.IntegerField(default=0)  # en minutos
    energia_consumida = models.FloatField(default=0.0)  # en kWh
    distancia_recorrida = models.FloatField(default=0.0)  # en metros
    temperatura = models.FloatField(default=0.0)  # en grados Celsius
    humedad = models.FloatField(default=0.0)  # en porcentaje

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"Estadísticas del {self.fecha.strftime('%d/%m/%Y %H:%M')}"

class AlertaRobot(models.Model):
    TIPOS_ALERTA = [
        ('bateria', 'Batería Baja'),
        ('temperatura', 'Temperatura Alta'),
        ('error', 'Error de Sistema'),
        ('mantenimiento', 'Mantenimiento Requerido'),
    ]

    fecha = models.DateTimeField(default=timezone.now)
    tipo = models.CharField(max_length=20, choices=TIPOS_ALERTA)
    descripcion = models.TextField()
    resuelta = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"
