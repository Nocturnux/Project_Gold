
from django.shortcuts import render, redirect
from .forms import CabinForm
from cabin.models import Cabin
from django.http import JsonResponse
from django.contrib import messages

def cabin(request):    
    cabin_list = Cabin.objects.all()    
    return render(request, 'cabin/index.html', {'cabin_list': cabin_list})

def change_status_cabin(request, cabin_id):
    cabin = Cabin.objects.get(pk=cabin_id)
    cabin.status = not cabin.status
    cabin.save()
    return redirect('cabin')

def create_cabin(request):
    form = CabinForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('cabin')    
    return render(request, 'cabin/create.html', {'form': form})

def detail_cabin(request, cabin_id):
    cabin = Cabin.objects.get(pk=cabin_id)
    data = { 'name': cabin.name, 'image': cabin.image.url, 'capacity': cabin.capacity, 'cabin_type': str(cabin.cabin_type), 'description': cabin.description,'value': cabin.value, } 
    return JsonResponse(data)


def delete_cabin(request, cabin_id):
    cabin = Cabin.objects.get(pk=cabin_id)
    try:
        cabin.delete()        
        messages.success(request, 'Cabaña eliminada correctamente.')
    except:
        messages.error(request, 'No se puede eliminar la cabaña.')
    return redirect('cabin')

# Create your views here.
