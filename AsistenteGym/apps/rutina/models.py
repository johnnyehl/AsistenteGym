from django.db import models
from django.template.defaultfilters import slugify
from apps.users.models import User 

class TimeStampModel(models.Model):

	user = models.ForeignKey(User, db_index=True, null=True, blank=True)
	descripcion = models.TextField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now = True)
	
	class Meta:
		abstract = True

class Dia(models.Model):

	nombre = models.CharField(max_length = 10)

	def __unicode__(self):
		return self.nombre 

class Musculo(models.Model):

	nombre = models.CharField(max_length=500)
	imagen = models.URLField()
	descripcion = models.TextField()

	def __unicode__(self):
		return self.nombre

class Rutina(TimeStampModel):

	nombre = models.CharField(max_length=200)
	slug = models.SlugField(editable = False, unique=True)#para manejar detalle

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.nombre)
		super(Rutina, self).save(*args, **kwargs)

class Ejercicio(models.Model):

	musculo = models.ForeignKey(Musculo)
	nombre = models.CharField(max_length=500)
	imagen = models.URLField()
	descripcion = models.TextField()

	def __unicode__(self):
		return self.nombre

	def imagen_ejercicio(self):
		return self.imagen


##############################################################
class DiaEntrenamiento(models.Model):

	rutina = models.ForeignKey(Rutina)
	dia = models.ForeignKey(Dia)


class MusculoEntrenamiento(models.Model):

	dia_entrenamiento = models.ForeignKey(DiaEntrenamiento)
	musculo = models.ForeignKey(Musculo)

	def __unicode__(self):
		return '%s ' % (self.id)


class MusculoEjercicio(models.Model):

	musculo_entrenamiento = models.ForeignKey(MusculoEntrenamiento)
	ejercicio = models.CharField(max_length=500)
	serie = models.IntegerField()
	repeticion =  models.IntegerField()
	peso = models.IntegerField()
	nivel = models.CharField(max_length=15)

	def __unicode__(self):
		return '%s ' % (self.id)
#############################################################