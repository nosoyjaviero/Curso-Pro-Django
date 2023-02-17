from django.shortcuts import render

# Create your views here.




#imaginemos que nos han pedido los siguientes requerimientos
 

# 1 requrimiento 
#-Lista todos los empleados de la empresa
#importamos ListView
from django.views.generic import (
    ListView
    )
# importamos el modelo con el que trabajaremos
from .models import Empleado
#creamos la clase correspondiente
#le indicamos que tipo de lista generica estaremos trabajando


class ListAllEmpleados(ListView):
    #debemos decirle de primero que template vamos a trabajar
    template_name= 'personas/list_all.html'
    # debemos indicarle con cual modelo vamos a trabajar 
    model= Empleado
    
    context_object_name='lista'

# 2-Listar todos los empleados que pertenecen a un area en la empresa

#El proposito de esta clase es devolver empleados segun el area especificada
class ListByAreaEmployes(ListView):
    """ Lista de empleado de un area"""
    template_name= 'personas/list_area.html'
    
    
    # Realizamos la consulta y se la asignamos la asignamos al objects_list para ser accedida en el archivo html
    queryset= Empleado.objects.filter(departamento_fk__short_name='Economia')
    
    #de una forma mas profesional aprendemos hacemos lo mismo pero de una manera mas profesional 
    
    def get_queryset(self):
        
        #Podemos capturar una variable que venga en una url atraves del siguiente paramento           
        area= self.kwargs['shortname']
        #luego se lo asignamos a departamento_fk__short_name (Ojo solo funciona si le pasamos el paramentro)
        
        lista= Empleado.objects.filter(
            departamento_fk__short_name=area)
        return lista
    
# 3- listar empleados por trabajo
# 4- listar los empleados por palabra clave
# 5- listar habilidades de un empleado