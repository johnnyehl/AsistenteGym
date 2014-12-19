from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AsistenteGym.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('apps.home.urls')),
    url(r'^', include('apps.users.urls', namespace='users')), #urls logout de apps users
    url(r'^', include('apps.rutina.urls')),
    url(r'^', include('apps.discuss.urls')),
    url(r'^', include('apps.matricula.urls')),
    url(r'^', include('apps.evolucion.urls')),

     #PYTHON SOCIAL AUTH
    url(r'^', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),
)
