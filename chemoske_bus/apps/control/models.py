from django.db import models
from flights.models import Trip
from park.models import Fleet


class Seat(models.Model):
    name = models.IntegerField()
    status = models.TextField()


class Control(models.Model):
    num_seat = models.ManyToManyField(Seat)
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    depar_time = models.TextField()
    arrival_time = models.TextField()
    degree_of_comf = models.CharField(max_length=100)
    num_of_custom = models.IntegerField()