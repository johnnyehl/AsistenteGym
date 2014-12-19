from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	url(r'^paquetes/$', PaqueteListView.as_view(), name='paquetes'),
	url(r'^matricula/(?P<id>[-\w]+)/$', 'apps.matricula.views.matricula', name='matricula'),
	url(r'^matriculado/$', 'apps.matricula.views.matriculado', name='matriculado'),
	url(r'^registrar-matricula/(?P<id_paquete>[-\w]+)/(?P<tipo>[-\w]+)/$', 'apps.matricula.views.registrar_matricula', name='registrar_matricula'),
 
)
