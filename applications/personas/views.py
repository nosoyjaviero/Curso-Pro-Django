from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls import reverse
# Create your views here.




#imaginemos que nos han pedido los siguientes requerimientos
 

# 1 requrimiento 
#-Lista todos los empleados de la empresa
#importamos ListView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView, 
    DeleteView
    )
# importamos el modelo con el que trabajaremos
from .models import Empleado
#creamos la clase correspondiente
#le indicamos que tipo de lista generica estaremos trabajando


class InicioView(TemplateView):
    """ vista que carga la pagina de inicio"""
    template_name= 'inicio.html'

class ListAllEmpleados(ListView):
    #debemos decirle de primero que template vamos a trabajar
    template_name= 'personas/list_all.html'
    # debemos indicarle con cual modelo vamos a trabajar 
    
    #digitamos esto, entonces si vamos a la url de este metodo, notaremos que solo mostrara 4 resultados pero si digitamos esto en el navegador
    # http://127.0.0.1:8000/listar-todo-empleados/?page=2    
    #notaremos que nos mostrara nuevo resultados
    paginate_by=4
    #tambien podemos ordenarlos en este caso lo hare por nombre pero tambien se puede por otra
    ordering='firts_name'
    # ya no sera necesario el modelo
    
    
    def get_queryset(self):
        # print ('****************')
        #cuando se da el boton de buscar, el servidor recive atraves de una solicitud request, EN esta solicitud viene incluida una variable llamada kword a esta la obtenemos por aca de esta manera
        # self nos llamamos a si mismos
        #request Llamamos a la solicitud request 
        #Get le indicamos atraves de cual metodo
        #get('kword','') especificamente por esto
        
        #en primera instacia cuando entramos a la vista, esta palabra clave es un vacio 
        
        palabra_clave= self.request.GET.get("kword", '') #el id y el name  en el html debe ser igual a esto 
        #imprimimos la palabra buscada en la terminal
        # ya no hacemos la impresion en terminal 
        
        
        # el return de este resultado lo obtendra el html como respuesta atraves de context_object_name='empleado'
        lista= Empleado.objects.filter(
            #primero necesitamos especificar que queremos filtrar de nuestra base de datos en nuestroo 
            #en este caso queremos filtrar full name
            
            # supongamos que queremos buscar lo siguiente: #jorge
            
            # si yo escribo: jo 
            # icontains busca los posibles resultados           
             
            
            firts_name__icontains=palabra_clave
        )
        
        
        return lista

# 2-Listar todos los empleados que pertenecen a un area en la empresa

#El proposito de esta clase es devolver empleados segun el area especificada
class ListByAreaEmployes(ListView):
    """ Lista de empleado de un area"""
    template_name= 'personas/list_area.html'
    
    
    # Realizamos la consulta y se la asignamos la asignamos al objects_list para ser accedida en el archivo html
    queryset= Empleado.objects.filter(departamento_fk__short_name='Economia')
    
    #de una forma mas profesional aprendemos hacemos lo mismo pero de una manera mas profesional 
    
    context_object_name='empleados'
    def get_queryset(self):
        
        #Podemos capturar una variable que venga en una url atraves del siguiente paramento           
        area= self.kwargs['shortname']
        #luego se lo asignamos a departamento_fk__short_name (Ojo solo funciona si le pasamos el paramentro)
        
        lista= Empleado.objects.filter(
            departamento_fk__short_name=area)
        
        return lista
    
    
# 3- listar empleados por trabajo
# 4- listar los empleados por palabra clave

class ListEmployeeByKword(ListView):
    #creamos el html en el sucederan los eventos
    
    template_name= 'personas/by_keyword.html'
    # debemos indicarle con cual modelo vamos a trabajar 
    #la variable a la que accede el codigo html-django 
    context_object_name='empleado'
    
    def get_queryset(self):
        # print ('****************')
        #cuando se da el boton de buscar, el servidor recive atraves de una solicitud request, EN esta solicitud viene incluida una variable llamada kword a esta la obtenemos por aca de esta manera
        # self nos llamamos a si mismos
        #request Llamamos a la solicitud request 
        #Get le indicamos atraves de cual metodo
        #get('kword','') especificamente por esto
        palabra_clave= self.request.GET.get('kword','')
        #imprimimos la palabra buscada en la terminal
        # ya no hacemos la impresion en terminal 
        
        
        # el return de este resultado lo obtendra el html como respuesta atraves de context_object_name='empleado'
        lista= Empleado.objects.filter(
            firts_name=palabra_clave)
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name= 'personas/lista_empleado.html'
    
    # al no tener el query set debe tener obligatoriamente un modelo    
    model= Empleado
    
    context_object_name='empleado'
    paginate_by=10
        

class ListaEmpleadosAdmin(ListView):
    template_name= 'personas/lista_empleado.html'
    
    # al no tener el query set debe tener obligatoriamente un modelo    
    model= Empleado
    
    context_object_name='empleado'
        
#estaremos trabajando con una relacion de ManyToMany 
class ListaHabilidadesEmpleado(ListView):
    #declarar el template con el vamos a trabajar
    template_name= 'personas/habilidades.html'
    #para ser leido en el html
    context_object_name= 'habilidades'
    
    
    def get_queryset(self):
        
        #traemos la palabra guardada en el input text cuyo name es kword y esta es enviada por request
        palabra_clave= self.request.GET.get('kword','')
        #la convertimos en int por que id trabaja solo con
        print(f'Palabra Clave {palabra_clave}')
        
        # django nos dice que este metodo nos sirve par devolver todas las hibilidades pero solo de una persona
        try:
          palabra_clave=int(palabra_clave)
          empleado= Empleado.objects.get(id=palabra_clave)
          Lista_habilidades= empleado.habilidad.all()
          return Lista_habilidades
        except:
          return []
        
        
        #seleccionamos el numero de empledo por el id 
        #accedemos a su variable Habilidad que es ManytoMany
        #y le pedimos que se traiga todo y lo guarde e una variable
        
        #lo retornamos y lo pintamos en el html 
        

class ListaEmployeeDetailView(DetailView):
    
    template_name = "personas/detail_empleado.html"
    model = Empleado
    
    # si  quisieramos enviar algo extra podemos hacer lo siguiente
    def get_context_data(self, **kwargs) :
        context = super(ListaEmployeeDetailView,self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context

    
#internamente django crea un form y necesita que le digitemos estas variables para realizarlo 
class EmpleadoCreateView(CreateView):
    #1. el modelo
    model = Empleado
    #2. el template con el que trabajaremos
    template_name = "personas/add.html"
    
    #3. los campos
    #es necesario añadir el siguiente campo para esta vista y este lo asiciamos con los nombres de los campos de del modelo
    # fields=['firts_name','last_name','job','departamento_fk']
    #con esto podemos traernos todos los campos del modelo sin escribir lo de arriba
    # fields=('__all__')
    
    #Modificamos los campos que se mostraran en el form manuelmente a como los seleccionaremos de models
    
    fields=['firts_name',
            'last_name',
            'job',
            'departamento_fk',
            'avatar',
            'habilidad'
            ]
    
    
    # 4.
    # EN EL METODO POST, Si utilizamos el la vista CreateView es importante indicar cual sera la paginaredirect 
    # success_url= '.'
    
    # para redirigir podemos accediendo a la url, pero es una mala practica
    
    #una buena practica de lo anterior mencionado es utilizar lo siguiente
    #en los parametros le indicamos la etiqueta name de un url
    #nombreDelAPP_name:url name especifica
    success_url= reverse_lazy('persona_app:inicio')
    
    
    #form_valid lo que hace es validar los datos del html y luego se ejecuta 
    def form_valid(self, form):
        
        # aqui guardamos los valores del html 
        #nos es recomendable hacer un doble guardado asi que        
        empleado=form.save(commit=False)
        #lo rellenamos
        empleado.full_name= f'{empleado.firts_name} {empleado.last_name}'
        # y finalmente lo gardamos
        empleado.save()
        
        
        return super(EmpleadoCreateView ,self ).form_valid(form)

#es la vista mas generica y solo se hace para hacer transicion de una pagina a otra
class EmpleadoSucessView(TemplateView):
    template_name = "personas/persona.html"

        

class EmpleadoUpdateView(UpdateView):
    template_name = "personas/update.html"
    model = Empleado
    
    fields=['firts_name',
            'last_name',
            'job',
            'departamento_fk',
            'avatar',
            'habilidad'
            ]
    
    success_url= reverse_lazy('persona_app:empleados-admin')
    
    def form_valid(self, form):     
       
             
        empleado=form.save(commit=False)
        empleado.full_name= f'{empleado.firts_name} {empleado.last_name}'
       
        empleado.save()       
        
        return super(EmpleadoUpdateView ,self ).form_valid(form)    
    
    def post(self, request, *args, **kwargs):
        
        self.object= self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "personas/delete.html"
    
    #se necesita la redireccion
    success_url= reverse_lazy('persona_app:empleados-admin')
    
    
    # def delete(self, request, *args, **kwargs):  
        
        
    #     print("*******SELF OBJECT**********")
    #     print(self)
        
    #     print("*******request OBJECT**********")
    #     print(request)
        
    #     print("*******args OBJECT**********")
    #     print(args)
        
    #     print("*******kwargs OBJECT**********")
    #     print(kwargs)  
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     return super(EmpleadoDeleteView, self).delete(
    #         request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     #especificado en la documentacion de django
        
        
    #     self.object= self.get_object()
    #     print("*******SELF OBJECT**********")
    #     print(self.object)
        
        
    #     # success_url= self.get_success_url()
    #     success_url= reverse('persona_app:success')
    #     print("*******success_url**********")
    #     print(success_url)
        
    #     self.object.delete()
    #     #especificado en la documentacion de django
        
    #     return HttpResponseRedirect(success_url)

    
# 5- listar habilidades de un empleado