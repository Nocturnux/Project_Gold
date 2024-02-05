from django import forms
from . models import Booking

from booking.models import Booking

class BookingForm(forms.ModelForm):
      
    class Meta:
        model = Booking
        fields = "__all__"
        exclude = ['state_booking', 'id_customer']
        labels = {
            'date_booking': 'Fecha reserva',
            'date_start': 'Fecha de inicio',
            'date_end': 'Fecha de finalización',
            'value': 'Valor',
            'state_booking': 'Estado de la reserva',                      
        }
        widgets = {
            'date_booking' : forms.DateInput(attrs={'type':'date'}),
            'date_start': forms.DateInput(attrs={'type':'date'}),
            'date_end': forms.DateInput(attrs={'type':'date'}),
            'value': forms.NumberInput(attrs={'placeholder': 'Valor de la reserva'}),
        }