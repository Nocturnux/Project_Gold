
from django.shortcuts import render, redirect

from cabin.models import Cabin

def cabin(request):    
    cabin_list = Cabin.objects.all()    
    return render(request, 'cabin/index.html', {'cabin_list': cabin_list})

def change_status_cabin(request, cabin_id):
    cabin = cabin.objects.get(pk=cabin_id)
    cabin.status = not cabin.status
    cabin.save()
    return redirect('books')
# Create your views here.
