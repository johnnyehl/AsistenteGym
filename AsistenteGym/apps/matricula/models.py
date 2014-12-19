from django.db import models
from django.template.defaultfilters import slugify
from apps.users.models import User 

class TimeStampModel(models.Model):

	user = models.ForeignKey(User, db_index=True, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True

class Paquete(models.Model):

	nombre = models.CharField(max_length=100)
	meses = models.IntegerField()
	costo = models.FloatField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now = True)


	def __unicode__(self):
		return '%s %s %s' % (self.nombre , self.meses, self.costo)

class TipoPago(models.Model):

	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(null=True)

	def __unicode__(self):
		return self.nombre 

class Matricula(TimeStampModel): # todos los atributos heredamos de TimeStampModel
	
	paquete = models.ForeignKey(Paquete)
	tipo_pago = models.ForeignKey(TipoPago)
	fecha_ini = models.DateTimeField(null=True)
	fecha_fin = models.DateTimeField(null=True) #aqui se guardara la cantidad de meses * 30
	estado = models.BooleanField(default=False)
	confirmacion = models.BooleanField(default=False)

	#def __unicode__(self):
		#return '%s  %s' % (self.paquete.nombre, self.tipo_pago.nombre)

