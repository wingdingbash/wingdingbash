from django.db import models

# Create your models here.
class city(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    desc = models.TextField()
    offer= models.BooleanField(default=False)