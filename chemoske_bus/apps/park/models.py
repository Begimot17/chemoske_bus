from django.db import models
from drivers.models import Driver
from routes.models import Route

class Fleet(models.Model):

    number = models.CharField(max_length=100)
    driver_1 = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver_1')
    driver_2 = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver_2')
    mileage = models.IntegerField()
    route= models.ForeignKey(Route, on_delete=models.CASCADE)
    num_of_flights_perform = models.IntegerField()
    date_of_next = models.DateField()
    date_of_last = models.DateField()
    current_flight = models.CharField(max_length=100)