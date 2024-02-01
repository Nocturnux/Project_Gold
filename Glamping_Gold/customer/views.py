
from django.shortcuts import render, redirect
from .forms import CustomerForm
from customer.models import Customer

from .forms import CustomerForm

def customer(request):    
    customer_list = Customer.objects.all()    
    return render(request, 'customer/index.html', {'customer_list': customer_list})

def change_status_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    customer.status = not customer.status
    customer.save()
    return redirect('customer')

def create_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer')    
    return render(request, 'customer/create.html', {'form': form})