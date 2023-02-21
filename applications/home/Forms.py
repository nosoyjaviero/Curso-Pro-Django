
from django import forms
from .models import Prueba

# importo con djaneiro  el form mfo
class PruebaForm(forms.ModelForm):

    class Meta:

        model = Prueba
        
        #otra vez fields
        #aqui le indicamos que atributos del modelos queremos convertirlo en formulario para que se muestre en el html
        fields = ('__all__')
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aqui'
                }
            )
        }
    
    # clean esobligatorio y despues de _ el atributo a validar
    def clean_cantidad(self):
        # extraemos la variable
        cantidad = self.cleaned_data['cantidad']
        # realizamos la consulta
        if cantidad <10:
            #si no cumple salte  este error
            raise forms.ValidationError("Ingrese un mayor numero a 10")
        return cantidad
    