from django.db import models

class Bus(models.Model):
    name = models.CharField(max_length=100)
    num_of_seat = models.IntegerField()


class Driver(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    num_of_fines = models.IntegerField()
    num_of_flights = models.IntegerField()
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    salary = models.IntegerField()
    degree_of_cong = models.CharField(max_length=100)
    degree_of_reliab = models.CharField(max_length=100)


