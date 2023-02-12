from django.apps import AppConfig


class PersonasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #debe nombrarse igual aque para no tener porblemas buscan el name en django
    name = 'applications.personas'
