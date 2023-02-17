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
    
    #digitamos esto, entonces si vamos a la url de este metodo, notaremos que solo mostrara 4 resultados pero si digitamos esto en el navegador
    # http://127.0.0.1:8000/listar-todo-empleados/?page=2    
    #notaremos que nos mostrara nuevo resultados
    paginate_by=4
    #tambien podemos ordenarlos en este caso lo hare por nombre pero tambien se puede por otra
    ordering='firts_name'
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

class ListEmployeeByKword(ListView):
    #creamos el html en el sucederan los eventos
    
    template_name= 'personas/by_keyword.html'
    # debemos indicarle con cual modelo vamos a trabajar 
    #la variable a la que accede el codigo html-django 
    context_object_name='empleado'
    
    def get_queryset(self):
        print ('****************')
        #cuando se da el boton de buscar, el servidor recive atraves de una solicitud request, EN esta solicitud viene incluida una variable llamada kword a esta la obtenemos por aca de esta manera
        # self nos llamamos a si mismos
        #request Llamamos a la solicitud request 
        #Get le indicamos atraves de cual metodo
        #get('kword','') especificamente por esto
        palabra_clave= self.request.GET.get('kword','')
        #imprimimos la palabra buscada en la terminal
        # ya no hacemos la impresion en terminal 
        
        
        # el return de este resultado lo obtendra el html como respuesta atraves de context_object_name='empleado'
        lista= Empleado.objects.filter(
            firts_name=palabra_clave)
        return lista
        
        
        
       
    
    

# 5- listar habilidades de un empleado