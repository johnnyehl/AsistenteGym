from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import View, DetailView
from django.core.mail import EmailMessage

from .forms import ExtraDataForm #importamos para utilizar formulario creado
from .models import User
from apps.discuss.models import Question
from apps.matricula.models import Matricula
from apps.rutina.models import Rutina

class ExtraDataView(View):

	def get(self, request, *args, **kwargs):
		if request.user.status:
			return redirect('/')
		else:
			return render(request, 'users/extra_data.html')#hacrivo que se encuentra en template/users/
		
	def post(self, request, *args, **kwargs): #utilizamos forms importado
		form = ExtraDataForm(request.POST)
		if form.is_valid():
			request.user.username = request.POST['username']
			request.user.email = request.POST['email']
			request.user.dni = request.POST['dni']
			request.user.status = True
			request.user.save()
			send_email(request) #envio de mail de saludo 
			return redirect('/')
		else:
			error_username = form['username'].errors.as_text()
			error_email = form['email'].errors.as_text()
			ctx = {'error_username':error_username, 'error_email': error_email}
			return render(request, 'users/extra_data.html', ctx)

def LogOut(request):
	logout(request)
	return redirect('/')
	
def send_email(request):

	msg = EmailMessage(subject='Bienvenid@',
								from_email = 'Asistente GYM <johnny.ehl@gmail.com',
								to=[request.user.email])

	msg.template_name = 'welcome'
	msg.template_content = {

		'std_content00' : '<h1> Hola %s Bienvenido a Asistente GYM </h1>' % request.user
	}

	msg.send()


class UserDetailView(DetailView):

	model = User
	context_object_name = 'user' ##cambiar contexto para utilizar user en lugar de object
	## object.username por user.username
	slug_field = 'username' ##le decimos que se esta enviando por el slug

	##metodo para pasar mas detalles que pertenecen a otro modelo
	def get_context_data(self, **kwargs):
		context = super(UserDetailView, self).get_context_data(**kwargs)

		questions = Question.objects.filter(user = context['object']).order_by('created')#filtrado por id usuario
		tags = [ question.tag.all() for question in questions ]##para traer todas los tag de las preguntas
		context['ques_tags']=zip(questions, tags)#uniendo los dos modelos creados

		context['matriculas'] = Matricula.objects.filter(user=context['object']).order_by('-created')[:1]
		mat = Matricula.objects.filter(user=context['object']).order_by('-created')[:1]
		context['mat'] = len(mat)
		context['rutinas'] = Rutina.objects.filter(user=context['object'])

		facebook = context['object'].social_auth.filter(provider='facebook')
		if facebook:
			context['facebook']= facebook[0].extra_data['id']#creamos una variable de tipo lista 

		twitter = context['object'].social_auth.filter(provider='twitter')
		if twitter:
			context['twitter']=twitter[0].extra_data['access_token']['screen_name']

		return context
