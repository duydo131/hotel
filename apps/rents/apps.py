from django.apps import AppConfig


class RentConfig(AppConfig):
    name = 'apps.rents'

    def ready(self):
        import apps.rents.signals
