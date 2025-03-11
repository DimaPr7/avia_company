from avia_company.settings.base import *
from dotenv import load_dotenv

DEBUG = False

# ALLOWED_HOSTS = ['avia-company.onrender.com','127.0.0.1', 'localhost']
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': str(os.getenv("POSTGRES_DB")),
        'USER': str(os.getenv("POSTGRES_USER")),
        'PASSWORD': str(os.getenv("POSTGRES_PASSWORD")),
        'HOST': str(os.getenv("POSTGRES_HOST")),
        'PORT': str(os.getenv("POSTGRES_DB_PORT")),
    }
}


