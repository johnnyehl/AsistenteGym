from django.contrib import admin
from .models import Paquete, TipoPago, Matricula

class MatriculaAdmin(admin.ModelAdmin):
	list_display = ('id','user','paquete')
	list_filter = ['user']
	search_fields = ['user__dni']

class PaqueteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'meses', 'costo')

class TipoPagoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')

admin.site.register(Paquete, PaqueteAdmin)
admin.site.register(TipoPago, TipoPagoAdmin)
admin.site.register(Matricula, MatriculaAdmin)
