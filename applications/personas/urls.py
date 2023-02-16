# creamos el archivo urls aqui
from django.urls import path

#a;adimos las url que utilizaremos
#siempre debemos llamar a nuestras vistas
from . import views

urlpatterns = [
    # mandar a llamar al archivo vistas
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    #anadimos la url
    path('lista-by-area', views.ListByAreaEmployes.as_view())
]
