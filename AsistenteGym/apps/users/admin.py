from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #importa paquete administrador
#para personalizar el administrador de usuario en bloques

from .models import User

class usuarioAdmin(admin.ModelAdmin):
	list_display = ('dni', 'username', 'first_name','last_name' ,'imagen_user')
	search_fields = ['dni']

	def imagen_user(self, obj):
		url = obj.imagen_usuario()
		tag = '<img width="100" height="100" src="%s">' %url
		return tag

	imagen_user.allow_tags = True


class UserAdmin(UserAdmin):#clase para administrador

	fieldsets = (
		('Usuario', {'fields' : ('username', 'password')}),
		('Informacion personal', {'fields' : ('dni',
									  'first_name',
									  'last_name',
									  'fecha_nacimiento',
									  'email',
									  'avatar',
									  'talla',
									  'apto',
									  'tipo')}),
		('Permisos', {'fields' : ('is_active',
									  'is_staff',
									  'is_superuser',
									  'groups',
									  'user_permissions')}),
		)

		

admin.site.register(User, usuarioAdmin)

