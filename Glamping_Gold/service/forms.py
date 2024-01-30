from django import forms
from . models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
            'image': 'Imagen',
            'description': 'Descripción',
            'value': 'Valor',
            'status': 'Estado',                      
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'image': forms.FileInput(attrs={'placeholder': 'Ingrese la imagen del servicio'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingresa la descripción'}),  
            'value': forms.TextInput(attrs={'placeholder': 'Ingresa el valor'}),         
        }