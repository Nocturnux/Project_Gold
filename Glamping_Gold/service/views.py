
from django.shortcuts import render, redirect

from service.models import Service

def service(request):    
    service_list = service.objects.all()    
    return render(request, 'service/index.html', {'service_list': service_list})

def change_status_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    service.status = not service.status
    service.save()
    return redirect('service')
# Create your views here.
