from django.contrib import admin
from .models import Evolucion

class EvolucionAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

admin.site.register(Evolucion, EvolucionAdmin)
