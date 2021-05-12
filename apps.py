from django.apps import AppConfig
import django.db


class SecondConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'second'
