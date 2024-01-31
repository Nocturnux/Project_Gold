from django.shortcuts import render, redirect

from booking.models import Booking

from .forms import BookingForm

def booking(request):    
    booking_list = Booking.objects.all()    
    return render(request, 'booking/index.html', {'booking_list': booking_list})

def change_status_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    booking.status = not booking.status
    booking.save()
    return redirect('booking')


def create_booking(request):
    form = BookingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('booking')    
    return render(request, 'booking/create.html', {'form': form})