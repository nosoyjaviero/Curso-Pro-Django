from django.shortcuts import render

# esta vista generica esta por un nivel mas  abajo de las que conocemos por que llama a generic.edi
# y ademas tiene las caractericas que tenia las vista Genericass
from django.views.generic.edit import FormView
# Create your views here.


from applications.personas.models import Empleado


from .models import Departamento



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
        
        
        # 
        depa = Departamento(     
            # name= Variable de models.Departamento
            # shortname = nombre en el form                         
            name= form.cleaned_data['departamento'],
            # name Variable de models.Departamento
            # shortname = nombre en el form 
            short_name= form.cleaned_data['shortname']
        )
        #finalmento lo guardamos
        depa.save()
        
        # asignamos a una variable los siguiente valores
        # name= Variable de models.Empleado
        # shortname = nombre en el form     
        nombre=form.cleaned_data['nombre']
        
        apellido= form.cleaned_data['apellido']
        Empleado.objects.create(
            # los asignamos nuestras variable en  models.Empleado a las variables que hemos creado con el nombre de nombre y apellido 
            firts_name=nombre,
            last_name=apellido,
            # el job lo dejamos como 1, ya que 
            job='1',
            # a esta variable hay que asignarle un modelo completo, este lo creamos en la variable depa
            departamento_fk=depa
            
        )
        
        
         
        return super(NewDepartamientoView, self).form_valid(form)


