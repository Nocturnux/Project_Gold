from django.db import models

class Cabin(models.Model):
    name = models.TextField(max_length=100)
    image = models.ImageField(upload_to='cabin_images', null=True)
    capacity = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    value = models.IntegerField()
    status = models.BooleanField(default=True)
    id_cabinType = models.ForeignKey('cabin_type.Cabin_type', on_delete=models.DO_NOTHING)

def __str__(self):
    return self.title
