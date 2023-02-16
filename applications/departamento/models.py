from django.db import models

# Create your models here.

class Departamento(models.Model):
    #editable=False sirva para que no lo podamos editar
    name =models.CharField('Nombre',max_length=50, blank=True)
    short_name= models.CharField('Nombre Corto', max_length=20,unique=True)
    anulate=models.BooleanField('Anulado',default=False)
    
    class Meta():
        #con esta linea en http://127.0.0.1:8000/admin/ observaremos que dira
        # 'Mi Departamento' en vez del nombre de la clase 'Departaento'.
        #con esto podemos poner los texto de la pagina en español y programar en ingles
        
        #esto sirve para cuando buscamos retroalimentacion de nuestro codigo en foros, ayuda a que personas de otros idiomas puedan leer nuestro codigo
        
        verbose_name='Mi Departamento'
        #con esta linea en caso de encontrar mas de un datos sabra que hay mas 
        #departamentos y pondra 'Areas de la empresa' como texto
        verbose_name_plural= 'Areas de la empresa'
        #como aparecera el ordanamito por columna
        ordering=['name']
        #esta linea evita que  entre estas dos variables sean iguales
        unique_together=('name','shor_name')
    
    def __str__(self):
        
        return str(self.id) +' - '+ self.name +' - '+  self.short_name