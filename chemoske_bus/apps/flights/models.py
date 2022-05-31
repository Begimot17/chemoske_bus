from django.db import models
from routes.models import Route


class Trip(models.Model):
    photo = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    popularity = models.CharField(max_length=100)
    occupancy = models.CharField(max_length=100)
    profitability = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
