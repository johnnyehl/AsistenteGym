from django.conf.urls import patterns, include, url
from .views import RutinaListView
from .models import Rutina, DiaEntrenamiento, Dia

urlpatterns = patterns('',

	url(r'^rutinas/$', RutinaListView.as_view(), name='rutinas'),
	url(r'^edit-rutina/(?P<id>[-\w]+)/$', 'apps.rutina.views.edit_rutina', name='edit_rutina'),
	url(r'^delete-rutina/(?P<id>[-\w]+)/$', 'apps.rutina.views.delete_rutina', name='delete_rutina'),

	url(r'^crear-rutina/$', 'apps.rutina.views.crear_rutina', name='crear_rutina'),
	url(r'^add-dia/(?P<id>[-\w]+)/$', 'apps.rutina.views.add_dia', name='add_dia'),
	url(r'^add-musculo/(?P<nombre>[-\w]+)/(?P<id>[-\w]+)/$', 'apps.rutina.views.add_musculo', name='add_musculo'),
	url(r'^delete-dia/(?P<nombre>[-\w]+)/(?P<id>[-\w]+)/$', 'apps.rutina.views.delete_dia', name='delete_dia'),#eliminar dia
	url(r'^delete-musculo/(?P<nombre>[-\w]+)/(?P<id>[-\w]+)/(?P<id_rutina>[-\w]+)/(?P<dia_nombre>[-\w]+)/$', 'apps.rutina.views.delete_musculo', name='delete_musculo'),#eliminar dia
	url(r'^delete-ejercicio/(?P<nombre>[-\w]+)/(?P<id_m>[-\w]+)/(?P<id_e>[-\w]+)/$', 'apps.rutina.views.delete_ejercicio', name='delete_ejercicio'),#eliminar ejercicio
	url(r'^add-ejercicio/(?P<nombre>[-\w]+)/(?P<id>[-\w]+)/$', 'apps.rutina.views.add_ejercicio', name='add_ejercicio'),

	url(r'^detalle-ejercicio/(?P<id_e>[-\w]+)/(?P<id_r>[-\w]+)/$', 'apps.rutina.views.detalle_ejercicio', name='detalle_ejercicio'),


	
	url(r'^rutina-dia/(?P<id>[-\w]+)/$', 'apps.rutina.views.rutina_dia', name='rutina_dia'),
	url(r'^rutina-detalle/(?P<id>[-\w]+)/$', 'apps.rutina.views.rutina_detalle', name='rutina_detalle'),

	#url ajax-json-jquery
	url(r'inicio-dia-ajax/$', 'apps.rutina.views.inicioDiaAjax', name='inicio_dia_ajax'),
	url(r'rutina-ajax/$', 'apps.rutina.views.RutinaDiaAjax', name='ruitina_dia_ajax'),
	url(r'add-dia-ajax/$', 'apps.rutina.views.addDiaAjax', name='add_dia_ajax'),
	url(r'inicio-musculo-ajax/$', 'apps.rutina.views.inicioMusculoAjax', name='inicio_musculo_ajax'),#inicio agregar musculo
	url(r'lista-musculo-ajax/$', 'apps.rutina.views.listaMusculoAjax', name='lista_musculo_ajax'),#ajax para cargar cbo 
	url(r'add-musculo-ajax/$', 'apps.rutina.views.addMusculoAjax', name='add_musculo_ajax'),#agregar musculo a dia entrenamiento

	url(r'inicio-ejercicio-ajax/$', 'apps.rutina.views.inicioEjercicioAjax', name='inicio_ejercicio_ajax'),#inicio agregar musculo
	url(r'lista-ejercicio-ajax/$', 'apps.rutina.views.listaEjercicioAjax', name='lista_ejercicio_ajax'),#agregar ejercicio a diaEjercicio
	url(r'add-ejercicio-ajax/$', 'apps.rutina.views.addEjercicioAjax', name='add_ejercicio_ajax'),#agregar ejercicio a musculo-ejercicio


	url(r'validar-matricula-ajax/$', 'apps.rutina.views.validarMatriculaAjax', name='validar-matricula-ajax'),

	url(r'^ejercicio/(?P<id>[-\w]+)/$', 'apps.rutina.views.ejercicio', name='ejercicio'),
	url(r'^musculo/(?P<id>[-\w]+)/$', 'apps.rutina.views.musculo', name='musculo'),
 
)
