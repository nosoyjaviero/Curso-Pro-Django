from django.apps import AppConfig


class DepartamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #debe nombrarse igual aque para no tener porblemas buscan el name en django
    name = 'applications.departamento'
