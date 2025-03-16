from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command


class AirlinesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'airlines'

    def ready(self):
        post_migrate.connect(load_initial_data, sender=self)

def load_initial_data(sender, **kwargs):
    try:
        call_command('loaddata', 'initial_data.json')
    except Exception as e:
        print("Ошибка загрузки фикстур:", e)