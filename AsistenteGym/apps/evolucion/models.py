from django.db import models
from django.template.defaultfilters import slugify
from apps.users.models import User
from apps.rutina.models import Rutina

class TimeStampModel(models.Model):

	user = models.ForeignKey(User, db_index=True, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True

class Evolucion(TimeStampModel): # todos los atributos heredamos de TimeStampModel
	
	instructor = models.IntegerField()
	peso = models.FloatField() 
	hombro = models.IntegerField()
	pecho = models.IntegerField()
	cintura = models.IntegerField()
	brazo = models.IntegerField()
	antebrazo = models.IntegerField()
	pierna = models.IntegerField()
	pantorrillas = models.IntegerField()
	gluteos = models.IntegerField()

	#def __unicode__(self):
		#return '%s %s %s' % (self.user , self.instructor, self.peso)
