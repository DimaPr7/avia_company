from .base import *

DEBUG = False

ALLOWED_HOSTS = ['avia-company.onrender.com',]
# ALLOWED_HOSTS = ['*'] '127.0.0.1', 'localhost'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB"),
        'USER': os.getenv("POSTGRES_USER"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'HOST': os.getenv("POSTGRES_HOST"),
        'PORT': os.getenv("POSTGRES_DB_PORT"),
    }
}

