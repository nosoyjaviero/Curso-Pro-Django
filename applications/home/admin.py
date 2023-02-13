from django.contrib import admin
#importamos el archivo donde hicimos el modelo
from .models import Prueba

# Register your models here.
#lo llamamos
admin.site.register(Prueba)
