from django.db import models

class booking_cabin(models.Model):
    value = models.IntegerField()
    cabin = models.ForeignKey('cabin.Cabin', on_delete=models.DO_NOTHING)
    booking = models.ForeignKey('booking.Booking', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
# Create your models here.
