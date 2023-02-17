# creamos el archivo urls aqui
from django.urls import path

#a;adimos las url que utilizaremos
#siempre debemos llamar a nuestras vistas
from . import views

urlpatterns = [
    # mandar a llamar al archivo vistas
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    #anadimos la url
    
    #si declaro esta variable <shortname>, puedo capturarla dentro de esta funcion con kwarg(')
    path('lista-by-area/<shortname>/', views.ListByAreaEmployes.as_view()),
    
    #especificamos como se llama la url para realizar 
    path('buscar-empleado/', views.ListEmployeeByKword.as_view())
    
]
