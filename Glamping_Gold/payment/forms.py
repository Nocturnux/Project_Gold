from django import forms
from . models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ['state_payment']
        labels = {
            'date': 'Fecha',
            'payment_method': 'Metodo de pago',
            'value': 'Valor', 
            'id_booking': 'Id reserva', 
                              
        }
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date'}),
            'payment_method': forms.TextInput(attrs={'placeholder': 'Ingresa el metodo de pago'}),
            'value': forms.TextInput(attrs={'placeholder': 'Ingresa el valor'}),  
            'id_booking' : forms.SelectMultiple(attrs={"placeholder":"Seleccione reserva"})               
        }