from django.shortcuts import render

# esta vista generica esta por un nivel mas  abajo de las que conocemos por que llama a generic.edi
# y ademas tiene las caractericas que tenia las vista Genericass
from django.views.generic.edit import FormView
# Create your views here.


class NewDepartamientoView(FormView):
    pass



