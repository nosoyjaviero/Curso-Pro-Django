# creamos el archivo urls aqui
from django.urls import path

#a;adimos las url que utilizaremos
#siempre debemos llamar a nuestras vistas
from . import views 
#declaramos el nombre de nuestro app_name par acceder a nuestro names
app_name= 'persona_app'

urlpatterns = [
    # mandar a llamar al archivo vistas
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    #anadimos la url
    
    #si declaro esta variable <shortname>, puedo capturarla dentro de esta funcion con kwarg(')
    path('lista-by-area/<shortname>/', views.ListByAreaEmployes.as_view()),
    
    #especificamos como se llama la url para realizar 
    path('buscar-empleado/', views.ListEmployeeByKword.as_view()),
    
    #añadimos la url
    path('lista-habilidades/', views.ListaHabilidadesEmpleado.as_view()),
    
    #añadimos la url
    # <pk> django recoge la variable pk automaticamente
    path('listaDetalle/<pk>', views.ListaEmployeeDetailView.as_view()),
    
    #añadimos la url
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    #aÑadimos name para poder ser accedidela desde las vistas
    path('success/', views.EmpleadoSucessView.as_view(), name='success'),
    
    
]
    
