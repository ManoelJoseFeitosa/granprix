from django.apps import AppConfig


class CoreConfig(AppConfig): # MUDOU O NOME DA CLASSE
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'          # MUDOU O NOME DO APP
