from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, View
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
#para controlar acceso a susuarios no logeados
from braces.views import LoginRequiredMixin
from .forms import MatriculaForm #importamos para utilizar formulario creado
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *


from apps.users.models import User

from .models import *

class PaqueteListView(ListView):

	model = Paquete
	context_object_name = 'paquetes'

def matricula(request, *args, **Kwargs):
	_username = request.user.username
	paquete_id = Kwargs['id']
	template = "matricula/matricula.html"
	usuario = User.objects.get(username=_username)
	matriculas = Matricula.objects.filter(user=usuario.id)
	paquete = Paquete.objects.get(id=paquete_id)

	mat_user = Matricula.objects.filter(user=usuario.id).order_by('-created')[:1]
	longitud = len(mat_user)

	for matricula in mat_user:
		if matricula.estado == False and matricula.confirmacion == False:
			no = True;
		if matricula.estado == False and matricula.confirmacion == True:
			lista_mat = True;



	print longitud
	return render_to_response(template, locals())

def matriculado(request, *args, **Kwargs):
	_username = request.user.username

	template = "matricula/matriculado.html"
	usuario = User.objects.get(username=_username)
	matriculas = Matricula.objects.filter(user=usuario.id)
	paquete = Paquete.objects.get(id=paquete_id)

	mat_user = Matricula.objects.filter(user=usuario.id).order_by('-created')[:1]
	longitud = len(mat_user)

	for matricula in mat_user:
		if matricula.estado == False:
			no = True;



	print longitud
	return render_to_response(template, locals())

	
def registrar_matricula(request, *args, **Kwargs): 
	_user = request.user
	paquete_id = Kwargs['id_paquete']
	tipo = Kwargs['tipo']
	print tipo
	paquete = Paquete.objects.get(id=paquete_id)
	cantidad = paquete.meses*30


	matricula = Matricula()
	matricula.user =User.objects.get(id=_user.id)
	matricula.paquete = Paquete.objects.get(id=paquete_id)
	matricula.tipo_pago = TipoPago.objects.get(nombre=tipo)
	matricula.estado =True
	matricula.fecha_fin = date.today() + timedelta(days=cantidad)
	
	if tipo == 'Visa':
		matricula.fecha_ini = date.today()
		matricula.fecha_fin = date.today() + timedelta(days=cantidad)
		matricula.confirmacion = True

	matricula.save()

	return HttpResponseRedirect("/matriculado/")

def matriculado(request, *args, **Kwargs):
	_username = request.user.username

	template = "matricula/matriculado.html"
	usuario = User.objects.get(username=_username)
	matriculas = Matricula.objects.filter(user=usuario.id)


	mat_user = Matricula.objects.filter(user=usuario.id)
	mat_true = Matricula.objects.filter(user=usuario.id, estado=True)
	longitud = len(mat_user)
	long_true = len(mat_true)

	no = False

	for matricula in matriculas:
		if matricula.estado == False:
			no = True;

	print no
		


	print longitud
	return render_to_response(template, locals())