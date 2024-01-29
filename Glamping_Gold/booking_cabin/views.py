from django.shortcuts import render
from django.shortcuts import render, redirect

from booking_cabin.models import booking_cabin

def booking_cabin(request):    
    booking_cabin_list = booking_cabin.objects.all()    
    return render(request, 'booking_cabin/index.html', {'booking_cabin_list': booking_cabin_list})

def change_status_book(request,booking_cabin_id):
    booking_cabin = booking_cabin.objects.get(pk=booking_cabin_id)
    booking_cabin.status = not booking_cabin.status
    booking_cabin.save()
    return redirect('booking_cabin')
# Create your views here.
