from django import forms
from . models import Book

from authors.models import Author

class CabinForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.filter(status=True).order_by('name'))
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ['status']
        labels = {
            'code': 'Código',
            'title': 'Título',
            'description': 'Descripción',
            'publication_date': 'Fecha de publicación',
            'price': 'Precio',
            'image': 'Imagen',
            'author': 'Autor',                      
        }
        widgets = {
            'code': forms.TextInput(attrs={'placeholder': 'Ingrese el código del libro'}),
            'title': forms.TextInput(attrs={'placeholder': 'Ingrese el título del libro'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingrese la descripción del libro'}), 
            'publication_date': forms.DateInput(attrs={'type':'date'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),          
            'image': forms.FileInput(attrs={'placeholder': 'Ingrese la imagen del libro'}),
        }