from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, 
     #añadimos CreateView 
    CreateView)

# Create your views here.

#importar mis modelos
from .models import Prueba
#lo importamos
from .Forms import PruebaForm

# Creamos la vista llamando al archivo html

class PruebaView(TemplateView):
    #indicamos la nueva ruta ./templates.home/prueba.html
    template_name='home/prueba.html'
    
    #usaremos listviews
    #para usar un snipet de list view instalamos djaniero en extenciones
    #y aqui escribimos: listview 
    #y se autocompleta el snippet
    
class PruebaListView(ListView):
        # poner siempre como primera variable "TEMPLATE_NAME"
        #le decemos que este es el archivo que va a interactuar
    template_name = "home/lista.html"
        
        #esta es a la variable que llamaremos en nuestro archivo y interactuaremos con ella
    context_object_name= 'listaNumeros'
        
        #diccionario
    queryset=['0','10','20','30']
        
        # esto es equivalente a         
        # return render(request,archivo ,{nombreVAR: diccionario})
        # return render(request, template_name ,{'listaNumeros':queryset})
    
class Lista_Prueba(ListView):
        # poner siempre como primera variable "TEMPLATE_NAME"
        template_name = "home/lista_prueba.html"
        #LLamamos al model        
        model = Prueba
        #variable a  para llamar en el archivo pero solo en el caso de listview
        context_object_name= 'lista'
        
 
#Usamos CreateView
class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    #debemos agregar esto simo nos marca un error
    
    # cambiamos esto 
    # fields=['titulo','subtitulo','cantidad']
    # por esto
    form_class=PruebaForm
    
    success_url='/'
     
class ResumenFoundationView(TemplateView):
    template_name= 'home/resume_foundation.html'

class Home1View(TemplateView):
    template_name= 'home/home1.html'
class Home2View(TemplateView):
    template_name= 'home/home2.html'
class Home3View(TemplateView):
    template_name= 'home/home3.html'
  
    
         
    