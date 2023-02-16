from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.


admin.site.register(Habilidades)
#Heredamos admin.ModelAdmin
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        #solo puedo llamar a los atributos que existen en mi modelo
        'firts_name',
        'last_name',
        'departamento_fk',
        'job',   
        #si necesitara inventarme una columna en django debo hacer:
        #full name no existe en modelos sera columna que nos inventamos con una funcion        
         'full_name'  
    )
    #sirve para renderizar una barra de busqueda
    search_fields=('first_name',)
    
    #a;adir filtros de busqueda 
    list_filter=('job', 'habilidad', )
    #solo sirve para relaciones muchos a muchos y sirve a;adir una barra de busqueda en la lista de habilidades que vamos a a;adir en caso de tener miles de habilidades por a;adir.
    filter_horizontal = ('habilidad',)
    #sirve para realizar un filtro de busqueda
    
    #nos inventaremos la columna menciona arriba con esta funcion     
    
    def full_name(self,obj):
        # print(obj)
        # print(obj.firts_name)
        # print(obj.last_name)
        # print(obj.job)
        return f'{obj.firts_name} {obj.last_name}'
    
    #esta linea y class EmpleadoAdmin() se fucionan y muestran una tabla en http://127.0.0.1:8000/admin/personas/empleado/
        
admin.site.register(Empleado, EmpleadoAdmin)