from django.db import models
from flights.models import Trip
from park.models import Fleet


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    num_seat = models.IntegerField()
    contact_info = models.CharField(max_length=100)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    depar_time = models.DateField()
    arrival_time = models.DateField()
    price = models.IntegerField()
    degree_of_comf = models.CharField(max_length=100)
    num_of_custom = models.IntegerField()
