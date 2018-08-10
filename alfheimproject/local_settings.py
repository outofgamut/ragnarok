import os
import json

from core.exceptions import RagnarokConfigError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    with open(os.path.join(BASE_DIR, 'alfheimproject/conf/config.json')) as config:
        CONFIG = json.load(config)
except FileNotFoundError:
    raise RagnarokConfigError('config.json not found. Did you forgot to add it?')

try:
    with open(os.path.join(BASE_DIR, 'alfheimproject/conf/secrets.json')) as secrets:
        SECRETS = json.load(secrets)
except FileNotFoundError:
    raise RagnarokConfigError('secrets.json not found. Did you forgot to add it?')

if CONFIG['security']['use_md5'] and CONFIG['security']['use_bcrypt']:
    raise RagnarokConfigError('Please select only one password hasher')

DEBUG = CONFIG['server']['conf']['debug']

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{engine}'.format(engine=SECRETS['db_engine']),
        'NAME': SECRETS['db_database'],
        'USER': SECRETS['db_username'],
        'PASSWORD': SECRETS['db_password'],
        'HOST': SECRETS['db_host'],
        'PORT': SECRETS['db_port'],
    }
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'main_api.permissions.AllowHostOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}