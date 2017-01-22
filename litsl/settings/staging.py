# settings/staging.py

import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] #os.environ["ALLOWED_HOSTS"]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_USER_PW"],
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '../static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..','static/')
#STATICFILES_DIRS = [
 #       os.path.join(BASE_DIR, "static"),
 #       'static/',
 #       ]
