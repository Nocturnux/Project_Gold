from django.db import models

class Payment(models.Model):
    date = models.DateField()
    payment_method = models.CharField(max_length=55)
    value = models.IntegerField()
    state_payment = models.CharField(max_length=25)
    id_booking = models.ForeignKey('booking.Booking', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.payment_method
