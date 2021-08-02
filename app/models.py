from django.db import models

# Create your models here.
from django.urls import reverse



class Details(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()

    def get_absolute_url(self):
        return reverse('app/list')


    class Meta:
        db_table='details'


