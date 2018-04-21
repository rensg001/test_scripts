from django.apps import AppConfig


class FirstAppConfig(AppConfig):
    name = 'first_app'

    def ready(self):
        from . import signals
