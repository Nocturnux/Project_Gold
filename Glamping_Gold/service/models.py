from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='service_images', null=True)
    description = models.TextField(max_length=255)
    value = models.IntegerField()
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
