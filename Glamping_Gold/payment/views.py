from django.shortcuts import render, redirect
from payment.models import Payment
from .forms import PaymentForm

def payment(request):    
    payment_list = Payment.objects.all()    
    return render(request, 'payment/index.html', {'payment_list': payment_list})

def change_status_payment(request, payment_id):
    payment = Payment.objects.get(pk=payment_id)
    payment.status = not payment.status
    payment.save()
    return redirect('payment')

def create_payment(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('payment')    
    return render(request, 'payment/create.html', {'form': form})