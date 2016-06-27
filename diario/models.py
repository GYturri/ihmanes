from django.db import models
from temp.models import Estacion

class Datin(models.Model):
	estacion = models.ForeignKey(Estacion)
	fecha = models.DateField(auto_now=False)
	seleccion = (
		('A', 'maxima'),
		('I', 'minima'),
		('P', 'precipitacion'),
	)
	nombre = models.CharField(max_length=1, choices=seleccion)
	valor = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
	def __str__(self):
		return self.tipo.nombre