from django.apps import AppConfig


class RoomConfig(AppConfig):
    name = 'apps.room'

    def ready(self):
        import apps.room.signals
