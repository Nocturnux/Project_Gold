from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    document = models.IntegerField(max_length=20, unique=True)
    cellphone = models.IntegerField(max_length=15)
    email = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
