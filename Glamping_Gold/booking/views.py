from django.contrib import messages

from django.shortcuts import render, redirect

from django.http import JsonResponse

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



def detail_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    data = { 'date_booking': booking.date_booking, 'date_start': booking.date_start, 'date_end': booking.date_end, 'value' : booking.value, 'state_booking' : booking.state_booking, 'id_customer' : str(booking.id_customer) }    
    return JsonResponse(data)



def delete_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    try:
        booking.delete()        
        messages.success(request, 'Reserva eliminada correctamente.')
    except:
        messages.error(request, 'No se puede eliminar la reserva porque está asociada a un servicio.')
    return redirect('booking')