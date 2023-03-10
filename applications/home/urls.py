# creamos el archivo urls aqui
from django.urls import path
from . import views

urlpatterns = [
    # mandar a llamar al archivo vistas
    path('home/', views.PruebaView.as_view() ),
    
    #llamamos al archivo de listview
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.Lista_Prueba.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
    path('resumen/', views.ResumenFoundationView.as_view() ),
    path('home1/', views.Home1View.as_view() ),
    path('home2/', views.Home2View.as_view() ),
    path('home3/', views.Home3View.as_view() ),
]
