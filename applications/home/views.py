from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Creamos la vista llamando al archivo html
class PruebaView(TemplateView):
    #indicamos la nueva ruta ./templates.home/prueba.html
    template_name='home/prueba.html'