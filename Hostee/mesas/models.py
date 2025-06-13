from django.db import models

class Mesa(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('reservada', 'Reservada'),
    ]

    numero = models.IntegerField(unique=True)
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mesa {self.numero} - {self.get_estado_display()}"
