# creamos el archivo urls aqui
from django.urls import path

#para llamar a nuestra vista debemos importar a la vista
from . import views


urlpatterns = [
    # path('departamento/', ),
    path('new-departamento/', views.NewDepartamientoView.as_view(), name='nuevo_departamento'),
    path('departamento-lista/', views.DepartamentoListView.as_view(), name='list_departamento'),
]
