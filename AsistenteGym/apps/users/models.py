from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UserManager(BaseUserManager): #clase manager de usuario creado

	def _create_user(self, username, email, password,  tipo, is_staff, is_superuser, **extra_fields):

		email = self.normalize_email(email)
		user = self.model(username=username, email=email, tipo=tipo, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
		user.set_password(password) #seteamos el password
		user.save(using = self._db) #grabamos el usuario
		return user

	def create_user(self, username, email, password=None,  tipo='alumno',**extra_fields): #usuario normal
		return self._create_user(username, email, password, tipo, False, False, **extra_fields)

	def create_superuser(self, username, email, password, tipo='administrador', **extra_fields): #usuario normal
		return self._create_user(username, email, password, tipo, True, True, **extra_fields)

		
class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(max_length=50, unique=True)
	dni = models.IntegerField(max_length=8, unique=True, null=True)
	email = models.EmailField(max_length=50, unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField(null=True, blank=True)
	avatar = models.URLField()
	talla = models.FloatField(null=True, blank=True)
	apto = models.BooleanField(default=False)#para evaluar si esta apto para matricularse
	status = models.BooleanField(default=False)
	tipo = models.CharField(max_length=50)

	objects = UserManager()

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'username' #requerido para logearme
	REQUIRED_FIELDS = ['email',] #requerido para registrarme

	def get_short_name(self):
		return self.username

	def imagen_usuario(self):
		return self.avatar

