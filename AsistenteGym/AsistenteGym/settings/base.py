#import os se elimina para ser reemplazado por unipath 
from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'r6_(rr_rd$wc9u!mpoty%g-kmp$&#fz^7e!xjavr%0!t2gk9$1'

#TUPLA PARA APLICACIONES NETAMENTE DE DJANGO
DJANGO_APPS=(
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	)

#PARA APLICACIONES DE TERCEROS
THIRD_PARTY_APPS = (
    'south',
    'social.apps.django_app.default',#instalarndo social login despues hay que sincronizar la db
    'djrill', #para emal de notificacion mandril
    #'debug_toolbar',
	)

#APLICACIONES LOCALES
LOCAL_APPS = (
    'apps.home',
    'apps.users',
    'apps.discuss',
    'apps.rutina',
    'apps.evolucion',
    'apps.matricula',
	)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'AsistenteGym.urls'

WSGI_APPLICATION = 'AsistenteGym.wsgi.application'

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#decir donde estan alojados los archivos .html (carpeta template)
TEMPLATE_DIRS = [BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'users.User' #que modelo de usuario personalizado vamos a utiliazar

AUTHENTICATION_BACKENDS = (
        'social.backends.facebook.FacebookAppOAuth2',
        'social.backends.facebook.FacebookOAuth2',
        'social.backends.twitter.TwitterOAuth',
        'django.contrib.auth.backends.ModelBackend',
    )

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/extra-data/' #pagina a donde nos redireccionara despues de la Autenticacion 
SOCIAL_AUTH_LOGIN_URL = '/error/' #variable que envia error al logearse

SOCIAL_AUTH_USER_MODEL = 'users.User' #VARIABLE QUE NOS DICE QUE MODELO DE USUARIO VAMOS A UTILIZAR
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email'] #variable permite que facebook retorne el email del usuario que se loguee pero twitter no devuelve email
SOCIAL_AUTH_PIPELINE = ( #tupla que contiene varios pipeline social auth
        'social.pipeline.social_auth.social_details',
        'social.pipeline.social_auth.social_uid',
        'social.pipeline.social_auth.auth_allowed',
        'social.pipeline.social_auth.social_user',
        'social.pipeline.user.get_username',
        'social.pipeline.user.create_user',
        'social.pipeline.social_auth.associate_user',
        'social.pipeline.social_auth.load_extra_data',
        'social.pipeline.user.user_details',
        'apps.users.pipelines.get_avatar', #pipeline creado por mi
    )

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend" #utilizar el emvio de mail que nos da mandril

#importamos los procesadores de contexto de django social auth
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (

        'social.apps.django_app.context_processors.backends',

    )