from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Creamos la lista llamando al archivo html
class PruebaView(TemplateView):
    template_name='prueba.html'