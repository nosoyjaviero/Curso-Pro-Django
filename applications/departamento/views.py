from django.shortcuts import render

# esta vista generica esta por un nivel mas  abajo de las que conocemos por que llama a generic.edi
# y ademas tiene las caractericas que tenia las vista Genericass
from django.views.generic.edit import FormView
# Create your views here.


# Importo el Formulario
from .forms import NewDepartamentoForm

class NewDepartamientoView(FormView):
    # indicamento con que archivo estaremos trabajndo
    template_name='departamento/new_departamento.html'
    #le indicamos con que form estaremos trabajando
    form_class= NewDepartamentoForm  
    
    #a donde la redigiremos 
    success_url='/'

    def form_valid(self, form):
        print('**********estamos en form valid**************')    
        return super(NewDepartamientoView, self).form_valid(form)


