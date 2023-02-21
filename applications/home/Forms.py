
from django import forms
from .models import Prueba

# importo con djaneiro  el form mfo
class PruebaForm(forms.ModelForm):

    class Meta:

        model = Prueba
        
        #otra vez fields
        #aqui le indicamos que atributos del modelos queremos convertirlo en formulario para que se muestre en el html
        fields = ('__all__')
