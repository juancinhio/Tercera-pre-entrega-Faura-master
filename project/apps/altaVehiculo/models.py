from django.db import models
from vehiculo.models import Vehiculo
from cliente.models import Cliente
from django.utils import timezone

# Create your models here.

class AltaVehiculo(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateTimeField(default=timezone.now, editable=False)
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.fecha} {self.vehiculo_id} {self.cliente_id} {self.nombre}"
