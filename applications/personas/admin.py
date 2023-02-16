from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.


admin.site.register(Habilidades)
#Heredamos admin.ModelAdmin
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'firts_name',
        'last_name',
        'departamento_fk',
        'job',        
    )
    
admin.site.register(Empleado, EmpleadoAdmin)