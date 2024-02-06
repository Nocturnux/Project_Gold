from django.shortcuts import render, redirect
from service.models import Service
from .forms import ServiceForm
from django.http import JsonResponse
from django.contrib import messages

def service(request):    
    service_list = Service.objects.all()    
    return render(request, 'service/index.html', {'service_list': service_list})

def change_status_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    service.status = not service.status
    service.save()
    return redirect('service')

def create_service(request):
    form = ServiceForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Servicio creado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al crear el Servicio.')        
        return redirect('service')    
    return render(request, 'service/create.html', {'form': form})

def detail_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    data = {  'image': service.image.url, 'name': service.name, 'description': service.description, 'value': service.value, 'status': service.status }    
    return JsonResponse(data)

def delete_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    try:
        service.delete()        
        messages.success(request, 'Servicio eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el servicio porque está asociada a una reserva.')
    return redirect('service')

def edit_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Servicio actualizado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar el Servicio.')        
        return redirect('service')    
    return render(request, 'service/editar.html', {'form': form})