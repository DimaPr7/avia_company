from .base import *

# Продакшн окружение, DEBUG = False
DEBUG = False

# Разрешенные хосты для продакшн
ALLOWED_HOSTS = ['avia-company.onrender.com', '127.0.0.1', 'localhost']

# Настройки базы данных для продакшн
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}
