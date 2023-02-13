from django.db import models

# Create your models here.

#creamos el modelo
class Prueba(models.Model):
    #creamos nuestros campos 
     #djaneiro snippets
      #mc
    titulo=models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
   #mi 
    cantidad = models.IntegerField()
    def __str__ (self):
        return self.titulo + '-' + self.subtitulo
    
    #py manage.py makemigrations
    #py manage.py migrate