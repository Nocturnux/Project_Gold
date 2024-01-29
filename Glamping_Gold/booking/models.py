from django.db import models

class Booking(models.Model):
    date_booking = models.DateField()
    date_start = models.DateField()
    date_end = models.DateField()
    value = models.IntegerField()
    state_booking = models.CharField(max_length=25)
    id_customer = models.ForeignKey('customer.Customer', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.date_booking