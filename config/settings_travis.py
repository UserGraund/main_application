from __future__ import unicode_literals

from config.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'main_app_travis',
        'USER': 'postgres',
        'HOST': '127.0.0.1',
        'PASSWORD': '',
        'PORT': '5432'
    }
}
