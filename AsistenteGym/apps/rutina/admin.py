from django.contrib import admin
from .models import Dia, Ejercicio, Musculo, Rutina, DiaEntrenamiento, MusculoEntrenamiento, MusculoEjercicio

class rutinaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'descripcion')

class ejercicioAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'imagen_ejercicios')

	def imagen_ejercicios(self, obj):
		url = obj.imagen_ejercicio()
		tag = '<img width="100" height="100" src="%s">' %url
		return tag

	imagen_ejercicios.allow_tags = True

admin.site.register(Dia)
admin.site.register(Ejercicio, ejercicioAdmin)
admin.site.register(Musculo)
admin.site.register(Rutina, rutinaAdmin)
admin.site.register(DiaEntrenamiento)
admin.site.register(MusculoEntrenamiento)
admin.site.register(MusculoEjercicio)