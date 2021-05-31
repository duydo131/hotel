from django.apps import AppConfig


class RentConfig(AppConfig):
    name = 'apps.notification'

    def ready(self):
        import apps.notification.signals
