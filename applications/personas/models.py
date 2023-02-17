from django.db import models
from applications.departamento.models import Departamento

# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    verbose_name='Mi Habilidad'
    verbose_name_plural= 'Habilidades'
    
    def __str__(self):
        return f'{str(self.id)} - {self.habilidad}' 
       
    
    
    
class Empleado(models.Model):
    """Modelo para la tabla empleado

    
    """
    
    JOB_CHOISES= {('1','Contador',),
                  ('2','ADMINISTRADOR'),
                  ('3','ECONOMISTA'),
                  ('4','OTROS')}
    
    firts_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=50,choices=JOB_CHOISES)
    departamento_fk = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidad= models.ManyToManyField(Habilidades)
    
    def __str__(self):
     return str(self.id) +' - '+self.firts_name +' - '+self.last_name +' - '+self.job +' - '+str(self.departamento_fk)