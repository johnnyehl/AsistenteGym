from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	url(r'^evolucion/$', 'apps.evolucion.views.ver_evolucion', name='ver_evolucion'),
	url(r'^registrar-evolucion/$', evolucionView.as_view()),
	url(r'^lista-evolucion/$', evolucionListView.as_view()),

	url(r'buscar-user-ajax/$', 'apps.evolucion.views.buscarUserAjax', name='buscar_user_ajax'),

	url(r'consulta-evolucion-ajax/$', 'apps.evolucion.views.consultaEvolucionAjax', name='consulta_evolucion_ajax'),#inicio agregar musculo
 
)
