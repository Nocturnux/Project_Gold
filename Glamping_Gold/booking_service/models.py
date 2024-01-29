from django.db import models

class Booking_service(models.Model):
    id_booking = models.ForeignKey('booking.Booking', on_delete=models.DO_NOTHING)
    id_service = models.ForeignKey('service.Service', on_delete=models.DO_NOTHING)
    value = models.IntegerField()
    

    def __str__(self):
        return self.name
# Create your models here.
