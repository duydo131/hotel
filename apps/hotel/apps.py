from django.apps import AppConfig


class HotelConfig(AppConfig):
    name = 'apps.hotel'

    def ready(self):
        import apps.hotel.signals
