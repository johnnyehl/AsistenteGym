from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.models import User

import json

from django.core import serializers
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from .models import *
from .forms import DiaEntrenamientoForm, CreateRutinaForm
from apps.users.models import User
from apps.matricula.models import Matricula
from braces.views import LoginRequiredMixin
from datetime import *

class RutinaListView(ListView):

	model = Rutina
	context_object_name = 'rutinas'

	def get_context_data(self, **kwargs):
		context = super(RutinaListView, self).get_context_data(**kwargs)
		context['ejercicios'] = Ejercicio.objects.all()[:6]
		return context


def delete_rutina(request, *args, **Kwargs): 
	rutina_id = Kwargs['id']


	rutina = Rutina.objects.get(id=rutina_id)
	rutina.delete()

	return HttpResponseRedirect("/rutinas/")

def edit_rutina(request, *args, **Kwargs):
	rutina_id = Kwargs['id']
	rutina = Rutina.objects.get(id=rutina_id)

	if request.method == "POST":
		form = CreateRutinaForm(request.POST,request.FILES)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']

			rutina.nombre = nombre
			rutina.descripcion = descripcion
			#Rutina = form.save(commit = False)
			rutina.user = request.user
			rutina.save()

			return HttpResponseRedirect("/add-dia/%s"%rutina.id)

	if request.method == "GET":
		form = CreateRutinaForm(initial={
			'nombre': rutina.nombre,
			'descripcion': rutina.descripcion,
			})

	ctx = {'form': form, 'rutina':rutina}
	template = "rutina/edit_rutina.html"
	return render_to_response(template, ctx, context_instance = RequestContext(request,locals()))


class DiaEntrenamientoCreateView(LoginRequiredMixin, CreateView):
	model = DiaEntrenamiento 
	success_url = '/'
	login_url = '/'

	def post(self, request, *args, **Kwargs):
		post = super(DiaEntrenamientoCreateView, self).post(request, *args, **Kwargs)
		rutina = Kwargs['id']
		dia = request.POST['dia']
		DiaEntrenamiento.objects.create(rutina=Rutina.objects.get(id=rutina) ,dia=Dia.objects.get(id=dia) )
		return post
########################################################
########################################################
def crear_rutina(request):

	if request.method == "POST":
		form = CreateRutinaForm(request.POST)
		if form.is_valid():
			Rutina = form.save(commit = False)
			Rutina.user = request.user
			Rutina.save()

			return HttpResponseRedirect("/add-dia/"+str(Rutina.id) )

	else:
		form = CreateRutinaForm()
	template = "rutina/crear_rutina.html"
	return render_to_response(template, context_instance = RequestContext(request,locals()))



def rutina_dia(request, *args, **Kwargs):
	rutina = Kwargs['id']
	if request.method == "POST":
		form = DiaEntrenamientoForm(request.POST)
		if form.is_valid():
			DiaEntrenamiento = form.save(commit = False)
			DiaEntrenamiento.rutina = Rutina.objects.get(id=rutina)
			DiaEntrenamiento.save()

			return HttpResponseRedirect("/rutina-detalle/"+rutina)

	else:
		form =DiaEntrenamientoForm()
	template = "rutina/form.html"
	#dias = Dia.objects.all()
	#entrenamientos = DiaEntrenamiento.objects.all()
	return render_to_response(template, context_instance = RequestContext(request,locals()))

def rutina_detalle(request, *args, **Kwargs):
	_username = request.user.username
	rutina_id = Kwargs['id']
	template = "rutina/rutina_detalle.html"
	rutina = Rutina.objects.get(id=rutina_id)
	diaentrenamiento = DiaEntrenamiento.objects.all()
	musculoentrenamiento = MusculoEntrenamiento.objects.all()
	musculoejercicio = MusculoEjercicio.objects.all()
	ejercicios = Ejercicio.objects.all()
	musculos = Musculo.objects.all()[:6]
	usuario = User.objects.get(username=_username)

	return render_to_response(template, locals())
#############################################################
		#DIA-ENTRENAMIENTO
		##################

def add_dia(request, *args, **Kwargs):
	_username = request.user.username
	rutina_id = Kwargs['id']
	template = "rutina/add_dia.html"
	rutina = Rutina.objects.get(id=rutina_id)
	usuario = User.objects.get(username=_username)
	return render_to_response(template, locals())

def RutinaDiaAjax(request, *args, **Kwargs): #Cargar dias en combo box
	rutina_id = request.GET['id']
	rutina = Rutina.objects.get(id = rutina_id)
	#print rutina.id
	de = DiaEntrenamiento.objects.filter(rutina = rutina.id)
	dia = Dia.objects.all()
	dias = Dia()
	l_id = [ ]
	l_nombre = [ ]
	#uno = 0
	#cargar dias al arreglo
	for d in dia:
		l_id.append(d.id)
		l_nombre.append(d.nombre) 
		#print l_nombre[uno]
		#uno+=1
	
	#print len(l_nombre)
	#remover los dias que ya se encuentran registrado
	for e in de:
		#print e.dia.id
		for d in dia:
			if e.dia.id == d.id:
				l_id.remove(d.id)
				l_nombre.remove(d.nombre) 
			#print d.id


	data = json.dumps(l_nombre)
	return HttpResponse(data, content_type='application/json')

def addDiaAjax(request, *args, **Kwargs): #agregar dia con json
	rutina_id = request.GET['id']
	dia_nombre = request.GET['nombre']

	#gravando
	d_e = DiaEntrenamiento()
	d_e.rutina = Rutina.objects.get(id = rutina_id)
	d_e.dia = Dia.objects.get(nombre = dia_nombre)
	d_e.save()

	#consulta para devolver lista
	dia_e= DiaEntrenamiento.objects.filter(rutina = rutina_id)
	print len(dia_e)
	
	#cargando lista con objeto filtrado
	arreglo = [ ]
	for d in dia_e:
		arreglo.append(d.dia.nombre) 

	data = json.dumps(arreglo)
	return HttpResponse(data, content_type='application/json')

def inicioDiaAjax(request, *args, **Kwargs):#carga los dias que se encuentran en dia entrenamiento al cargar la pagina
	rutina_id = request.GET['id']

	#consulta para devolver lista
	dia_e= DiaEntrenamiento.objects.filter(rutina = rutina_id)
	print len(dia_e)
	
	#cargando lista con objeto filtrado
	arreglo = [ ]
	for d in dia_e:
		arreglo.append(d.dia.nombre) 

	data = json.dumps(arreglo)
	return HttpResponse(data, content_type='application/json')


def delete_dia(request, *args, **Kwargs): #eliminar dia

	dia_nombre = Kwargs['nombre']
	rutina_id = Kwargs['id']
	dia = Dia.objects.get(nombre=dia_nombre)
	d_e = DiaEntrenamiento.objects.get(dia=dia.id,rutina=rutina_id)
	d_e.delete()

	return HttpResponseRedirect("/add-dia/"+rutina_id)

#####################################################################################################
			#MUSCULO-ENTRENAMIENTO
			######################
def add_musculo(request, *args, **Kwargs):
	_username = request.user.username
	dia_nombre = Kwargs['nombre']
	rutina_id = Kwargs['id']
	print dia_nombre
	template = "rutina/add_musculo.html"
	dia = Dia.objects.get(nombre=dia_nombre)

	d_e = DiaEntrenamiento.objects.get(dia=dia.id,rutina=rutina_id)
	usuario = User.objects.get(username=_username)

	return render_to_response(template, locals())

def inicioMusculoAjax(request, *args, **Kwargs):#carga los dias que se encuentran en dia entrenamiento al cargar la pagina
	dia_entrenamiento_id= request.GET['id']

	#consulta para devolver lista
	m_e= MusculoEntrenamiento.objects.filter(dia_entrenamiento= dia_entrenamiento_id)
	print len(m_e)
	
	#cargando lista con objeto filtrado
	arreglo = [ ]
	for m in m_e:
		arreglo.append(m.musculo.nombre) 

	data = json.dumps(arreglo)
	return HttpResponse(data, content_type='application/json')

def listaMusculoAjax(request, *args, **Kwargs): #Cargar dias en combo box
	dia_entrenamiento = request.GET['id']
	d_e = DiaEntrenamiento.objects.get(id = dia_entrenamiento)
	#print rutina.id
	de = MusculoEntrenamiento.objects.filter(dia_entrenamiento = dia_entrenamiento)
	musculo = Musculo.objects.all()

	m_nombre = [ ]
	#uno = 0
	#cargar dias al arreglo
	for m in musculo:
		m_nombre.append(m.nombre) 
		#print l_nombre[uno]
		#uno+=1
	
	#print len(l_nombre)
	#remover los dias que ya se encuentran registrado
	for e in de:
		#print e.dia.id
		for m in musculo:
			if e.musculo.id == m.id:
				m_nombre.remove(m.nombre) 
			#print d.id


	data = json.dumps(m_nombre)
	return HttpResponse(data, content_type='application/json')

def addMusculoAjax(request, *args, **Kwargs): #agregar dia con json
	dia_entrenamiento = request.GET['id']
	musculo_nombre = request.GET['nombre']

	#gravando
	m_e = MusculoEntrenamiento()
	m_e.dia_entrenamiento = DiaEntrenamiento.objects.get(id = dia_entrenamiento)
	m_e.musculo = Musculo.objects.get(nombre = musculo_nombre)
	m_e.save()

	#consulta para devolver lista
	musculo_e= MusculoEntrenamiento.objects.filter(dia_entrenamiento = dia_entrenamiento)
	
	#cargando lista con objeto filtrado
	arreglo = [ ]
	for m in musculo_e:
		arreglo.append(m.musculo.nombre) 

	data = json.dumps(arreglo)
	return HttpResponse(data, content_type='application/json')


def delete_musculo(request, *args, **Kwargs): #eliminar dia

	musculo_nombre = Kwargs['nombre']
	dia_entrenamiento = Kwargs['id']
	rutina_id = Kwargs['id_rutina']
	dia_nombre = Kwargs['dia_nombre']

	musculo = Musculo.objects.get(nombre=musculo_nombre)
	de = DiaEntrenamiento.objects.get(id=dia_entrenamiento)
	m_e = MusculoEntrenamiento.objects.get(musculo=musculo.id, dia_entrenamiento=de.id )
	m_e.delete()

	return HttpResponseRedirect("/add-musculo/"+dia_nombre+"/"+rutina_id)

########################################################################################################
		  #EJERCICIO-MUSCULO
		  ##################

def add_ejercicio(request, *args, **Kwargs):
	_username = request.user.username
	musculo_nombre = Kwargs['nombre']
	d_e_id = Kwargs['id']
	template = "rutina/add_ejercicio.html"
	musculo = Musculo.objects.get(nombre=musculo_nombre)
	ejercicio = Ejercicio.objects.all()

	m_e = MusculoEntrenamiento.objects.get(musculo=musculo.id,dia_entrenamiento=d_e_id)
	usuario = User.objects.get(username=_username)
	return render_to_response(template, locals())

def listaEjercicioAjax(request, *args, **Kwargs): #Cargar dias en combo box
	musculo_entrenamiento = request.GET['id']
	musculo_id = request.GET['musculo']
	
	print "hola"+musculo_id
	m_ejercicio = MusculoEjercicio.objects.filter(musculo_entrenamiento = musculo_entrenamiento)
	ejercicio = Ejercicio.objects.filter(musculo=musculo_id)
	print len(ejercicio)
	e_nombre = [ ]
	#uno = 0
	#cargar dias al arreglo
	for e in ejercicio:
		e_nombre.append(e.nombre) 
		#print l_nombre[uno]
		#uno+=1
	
	print len(e_nombre)
	#remover los dias que ya se encuentran registrado
	for m in m_ejercicio:
		#print e.dia.id
		for e in ejercicio:
			if m.ejercicio == e.nombre:
				e_nombre.remove(e.nombre) 
			#print d.id


	data = json.dumps(e_nombre)
	return HttpResponse(data, content_type='application/json')


def addEjercicioAjax(request, *args, **Kwargs): #agregar dia con json
	musculo_entrenamiento = request.GET['id']
	#ejercicio = request.GET['ejercicio']
	#gravando
	m_e = MusculoEjercicio()
	m_e.musculo_entrenamiento = MusculoEntrenamiento.objects.get(id = musculo_entrenamiento)
	m_e.ejercicio = request.GET['ejercicio']
	#print m_e.ejercicio
	m_e.serie = request.GET['serie']
	m_e.repeticion = request.GET['repeticion']
	
	m_e.peso = request.GET['peso']
	m_e.nivel = request.GET['nivel']
	m_e.save()

	#consulta para devolver lista
	#musculo_e= MusculoEjercicio.objects.filter(musculo_entrenamiento = musculo_entrenamiento)
	
	musculo_entrenamiento = MusculoEntrenamiento.objects.get(id =request.GET['id'])

	musculo_e = MusculoEjercicio.objects.filter(musculo_entrenamiento = musculo_entrenamiento)
	data = serializers.serialize('json', musculo_e,
			fields = {'id', 'ejercicio', 'serie', 'repeticion', 'peso', 'nivel'})
	return HttpResponse(data, content_type='application/json')

def inicioEjercicioAjax(request, *args, **Kwargs):#carga los dias que se encuentran en dia entrenamiento al cargar la pagina

	musculo_entrenamiento = MusculoEntrenamiento.objects.get(id =request.GET['id'])
	
	musculo_e = MusculoEjercicio.objects.filter(musculo_entrenamiento = musculo_entrenamiento)
	for m in musculo_e:
		print m.pk

	data = serializers.serialize('json', musculo_e,
			fields = {'pk', 'musculo_entrenamiento', 'ejercicio', 'serie', 'repeticion', 'peso', 'nivel'})
	return HttpResponse(data, content_type='application/json')

def delete_ejercicio(request, *args, **Kwargs): #FALTA FILTRO PARA ELIMINAR ... SE TIENE QUE CONSIDERAR ID MUSCULO_ENTRENAMIENTO Y MUSCULO_EJERCICIO
	musculo_entrenamiento_id = Kwargs['id_m']
	musculo_e_id = Kwargs['id_e']
	nombre = Kwargs['nombre']

	m_e = MusculoEjercicio.objects.get(id=musculo_e_id)
	m_e.delete()

	return HttpResponseRedirect("/add-ejercicio/"+nombre+"/"+musculo_entrenamiento_id)

#################################################################################################################################################
	#EJERCICIO-DETALLE

def detalle_ejercicio(request, *args, **Kwargs):
	_username = request.user.username
	ejercicio_id = Kwargs['id_e']
	rutina_id = Kwargs['id_r']
	template = "rutina/detalle_ejercicio.html"
	ej = Ejercicio.objects.get(id=ejercicio_id)
	rutina = Rutina.objects.get(id=rutina_id)
	usuario = User.objects.get(username=_username)

	return render_to_response(template, locals())





#####################################################################################
	###FUNCION QUE SE EJECUTA CADA VEZ QUE INICIE EL SISTEMA
#####################################################################################

def validarMatriculaAjax(request, *args, **Kwargs): #Cargar dias en combo box
	
	_user_id = request.user.id
	
	matriculas = Matricula.objects.filter(user=_user_id,estado=True)

	estado = ""
	#hoy = datetime.now()-timedelta(days=1)
	hoy = datetime.now()

	print hoy.strftime('%Y-%m-%d')


	for matricula in matriculas:
		print matricula.fecha_fin.strftime('%Y-%m-%d')
		if matricula.fecha_fin.strftime('%Y-%m-%d') == hoy.strftime('%Y-%m-%d'):
			matricula.estado = False
			matricula.save()
			estado ="True"	
			
	data = json.dumps(estado)
	return HttpResponse(data, content_type='application/json')


#####Ejercicios detalle

def ejercicio(request, *args, **Kwargs):
	ejercicio_id = Kwargs['id']

	template = "rutina/ejercicio.html"
	ej = Ejercicio.objects.get(id=ejercicio_id)
	

	return render_to_response(template, locals())



def musculo(request, *args, **Kwargs):
	ejercicio_id = Kwargs['id']

	template = "rutina/musculo.html"
	ej = Musculo.objects.get(id=ejercicio_id)
	

	return render_to_response(template, locals())

