from django.shortcuts import render

def bookin_service(request):
    return render(request, 'booking_service/index.html')

from django.shortcuts import render, redirect

from booking_service.models import Booking_service

def booking_service(request):    
    booking_service_list = Booking_service.objects.all()    
    return render(request, 'booking_service/index.html', {'booking_service_list': booking_service_list})

def change_status_booking_service(request, booking_service_id):
    booking_service = Booking_service.objects.get(pk=booking_service_id)
    booking_service.status = not booking_service.status
    booking_service.save()
    return redirect('booking_service')
# Create your views here.
