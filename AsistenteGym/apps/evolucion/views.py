from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
#para controlar acceso a susuarios no logeados
from braces.views import LoginRequiredMixin

import json

from apps.users.models import User
from apps.rutina.models import Rutina
from apps.matricula.models import Matricula
from .models import Evolucion
from .forms import *


def ver_evolucion(request, *args, **Kwargs):
	_username = request.user.username
	template = "evolucion/evolucion.html"
	usuario = User.objects.get(username=_username)
	usuarios = User.objects.all()
	evoluciones = Evolucion.objects.filter(user = usuario.id).order_by('-created')[:12]
	matriculas = Matricula.objects.filter(user=usuario.id).order_by('-created')[:1]
	longitud = len(evoluciones)
	longi = len(matriculas)

	no_confirmado = False
	no = False

	if longi == 0:
		no = True

	for matricula in matriculas:
		if matricula.confirmacion == False:
			no_confirmado = True

	if longitud > 0:
		ideal = (usuario.talla - 1.08)*100
				
		
	
	

	

	

	return render_to_response(template, locals())

class evolucionView(CreateView):
	template_name = 'evolucion/registrar_evolucion.html'
	model = Evolucion
	form_class = evolucionForm
	success_url = 'evolucion/lista-evolucion/'

	def post(self, request, *args, **Kwargs):
		post = super(evolucionView,self).post(request, *args, **Kwargs)
		ins = request.user
		instructor=User.objects.get(id=ins.id)
		inst_id = instructor.id
		
		dni = request.POST['user']
		peso = float(request.POST['peso'])
		hombro = float(request.POST['hombro'])
		pecho = float(request.POST['pecho'])
		cintura = float(request.POST['cintura'])
		brazo = float(request.POST['brazo'])
		antebrazo = float(request.POST['antebrazo'])
		pierna = float(request.POST['pierna'])
		pantorrillas = float(request.POST['pantorrillas'])
		gluteos = float(request.POST['gluteos'])

		Evolucion.objects.create( user=User.objects.get(dni=dni), instructor=inst_id, peso=peso, hombro=hombro, pecho=pecho, 
			cintura=cintura, brazo=brazo, antebrazo=antebrazo, pierna=pierna, pantorrillas=pantorrillas, gluteos=gluteos)
		return HttpResponseRedirect("/lista-evolucion/")

class evolucionListView(ListView):
	template_name = 'evolucion/lista_evolucion.html'
	model = Evolucion
	context_object_name = 'evoluciones'

def buscarUserAjax(request, *args, **Kwargs):#carga los dias que se encuentran en dia entrenamiento al cargar la pagina

	dni = User.objects.filter(dni =request.GET['dni'], apto=True)
	no_apto = User.objects.filter(dni =request.GET['dni'], apto=False)
	print len(dni)
	arreglo = [ ]
	if len(dni) == 1:
		arreglo.append("apto");

	if len(no_apto) == 1:
		arreglo.append("no apto");

	if len(dni)==0 and len(no_apto) == 0:
		arreglo.append("null");

	data = json.dumps(arreglo)
	return HttpResponse(data, content_type='application/json')


def consultaEvolucionAjax(request, *args, **Kwargs):
	
	evolucion = Evolucion.objects.filter(user =request.GET['id'])

	data = serializers.serialize('json', evolucion,
			fields = {'created','instructor', 'peso', 'hombro', 'pecho', 'cintura', 'brazo', 'antebrazo','pierna','pantorrillas','gluteos'})
	return HttpResponse(data, content_type='application/json')
