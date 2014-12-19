from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Gimnasio',
        'USER' : 'tucarnal',
        'PASSWORD' : 'jpoahtnyny',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')] #hace referencia a la carpeta static
#** CREAR APP EN LA PAGINA DE DEVELOPER FACEBOOK Y EN TWITTER
#https://developers.facebook.com
SOCIAL_AUTH_FACEBOOK_KEY = '668950696552178'
SOCIAL_AUTH_FACEBOOK_SECRET = '99e67d853c8fcf4bdf85adc02181ff54'

SOCIAL_AUTH_TWITTER_KEY = '5jRQyEaynMPWxPUuqMJlk9boo'
SOCIAL_AUTH_TWITTER_SECRET = 'SOnGsztmtuyFe7tNi03sBszwIc5MQmzFAN3O7QxCtOxuVlwWqA'
#mandrillapp.com johnny.ehl@gmail.com - j***************** y mandrillapp.com - tucarnal123 j*********-****/JO***A
MANDRILL_API_KEY = 'Gn0qdkJ_ZCcrZwpGzsGumQ'