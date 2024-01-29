
from django.shortcuts import render, redirect

from customer.models import Customer

def customer(request):    
    customer_list = Customer.objects.all()    
    return render(request, 'customer/index.html', {'customer_list': customer_list})

def change_status_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    customer.status = not customer.status
    customer.save()
    return redirect('customer')