from .base import *
from django.apps import AppConfig




# BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



DB_FILE = BASE_DIR.child('db.sqlite3')
# DB_FILE =os.path.join(BASE_DIR, 'db.sqlite3')


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     #aplicamos este comentario por que nos da complictos con la ruta (solucionar)
    #     # 'NAME': DB_FILE / 'db.sqlite3',
    #     'NAME': DB_FILE ,
    # }
    'default': {
        'ENGINE':'django.backend.postgresql_psycopg2',
        'NAME':'dbempleado',
        'USER':'neunapp',
        'PASSWORD':'123',
        'HOST':'localhost',
        'PORT':'5432',        
    }
    
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
