from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField
    bookingDate = models.DateTimeField(auto_now_add=True)


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    inventory = models.IntegerField()