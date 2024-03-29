from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'prueba',
        'USER': 'postgres',
        'PASSWORD': '123.abcd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
#STATIC_ROOT = BASE_DIR.child ('staticfiles', 'media')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')


