from django.db import models

class Estacion(models.Model):
	nombre = models.CharField(max_length=15)
	codigo = models.CharField(max_length=6)
	codpuno = models.CharField(max_length=2,default="00", null=True, blank=True)
	def __str__(self):
		return "%s - %s- %s" % (self.id, self.codigo, self.nombre)

class TermoPlu(models.Model):
	fecha = models.DateField(auto_now = False)
	estacion = models.ForeignKey(Estacion)
	maxi = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
	mini = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
	prec = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
	t1 = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
	t2 = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
	t3 = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
	def __str__(self):
		return "%s - %s --- MAX= %s MIN= %s PP= %s" % (self.fecha, self.estacion, self.maxi, self.mini, self.prec)