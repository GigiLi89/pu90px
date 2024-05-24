from django.apps import AppConfig


class AlbumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'album'


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals  # noqa