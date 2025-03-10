from .base import *

# Локальная разработка, DEBUG = True
DEBUG = True

# Разрешенные хосты для разработки
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
