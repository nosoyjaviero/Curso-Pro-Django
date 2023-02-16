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

# 2-Listar todos los empleados que pertenecen a un area ed la empresa
# 3- listar empleados por trabajo
# 4- listar los empleados por palabra clave
# 5- listar habilidades de un empleado

