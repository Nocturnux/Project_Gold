
from django.shortcuts import render, redirect
from .forms import Cabin_typeForm
from cabin_type.models import Cabin_type
from django.http import JsonResponse
from django.contrib import messages

def cabin_type(request):    
    cabin_type_list = Cabin_type.objects.all()    
    return render(request, 'cabin_type/index.html', {'cabin_type_list': cabin_type_list})

def change_status_cabin_type(request, cabin_type_id):
    cabin_type = Cabin_type.objects.get(pk=cabin_type_id)
    cabin_type.status = not cabin_type.status
    cabin_type.save()
    return redirect('cabin_type')


def create_cabin_type(request):
    form = Cabin_typeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cabin_type')    
    return render(request, 'cabin_type/create.html', {'form': form})

def detail_cabin_type(request, cabin_type_id):
    cabin_type = Cabin_type.objects.get(pk=cabin_type_id)
    data = { 'name': cabin_type.name }    
    return JsonResponse(data)


def delete_cabin_type(request, cabin_type_id):
    cabin_type = Cabin_type.objects.get(pk=cabin_type_id)
    try:
        cabin_type.delete()        
        messages.success(request, 'Tipo de cabaña eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el tipo de cabaña porque está asociado a una cabaña.')
    return redirect('cabin_type')