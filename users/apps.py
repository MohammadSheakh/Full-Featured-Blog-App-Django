from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): # django doc amader ke evabei import korte bolse
        import users.signals
