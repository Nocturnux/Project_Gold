from django.shortcuts import render
from django.shortcuts import render, redirect

from service.models import Service

def service(request):    
    service_list = Service.objects.all()    
    return render(request, 'service/index.html', {'service_list': service_list})

def change_status_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    service.status = not service.status
    service.save()
    return redirect('service')

from .forms import ServiceForm

def create_service(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('service')    
    return render(request, 'service/create.html', {'form': form})
