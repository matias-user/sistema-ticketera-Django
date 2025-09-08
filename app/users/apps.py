from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

# Para generar automáticamente el Perfil cuando se crea un usuario
    def ready(self):
        import users.signals    