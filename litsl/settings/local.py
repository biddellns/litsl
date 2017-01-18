# settings/local.py

import os

from .base import *

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += ("debug_toolbar", )

MIDDLEWARE = ('debug_toolbar.middleware.DebugToolbarMiddleware', )

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        'static/',
        ]

# Internal IPs for django_debug_toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]
