from django import forms
from . models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ['status','id_booking','state_payment']
        labels = {
            'date': 'Fecha',
            'payment_method': 'Metodo de pago',
            'value': 'Valor',  
                              
        }
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'Ingresa la fecha'}),
            'payment_method': forms.TextInput(attrs={'placeholder': 'Ingresa el metodo de pago'}),
            'value': forms.IntegerField(),                 
        }