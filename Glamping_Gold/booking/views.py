from django.shortcuts import render

def booking(request):
    return render(request, 'booking/index.html')

from django.shortcuts import render, redirect

from booking.models import Booking

def booking(request):    
    booking_list = Booking.objects.all()    
    return render(request, 'booking/index.html', {'booking_list': booking_list})

def change_status_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    booking.status = not booking.status
    booking.save()
    return redirect('booking')