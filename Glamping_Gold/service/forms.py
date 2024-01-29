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
            'description': 'Descripcion',
            'value': 'Valor',
            'status': 'Estado',                      
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'image': forms.TextInput(attrs={'placeholder': 'Ingresa la imagen'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingresa la descripcion'}),  
            'value': forms.TextInput(attrs={'placeholder': 'Ingresa el valor'}),
            'status': forms.TextInput(attrs={'placeholder': 'Ingresa el estado'}),          
        }