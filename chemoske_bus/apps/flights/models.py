from django.db import models
from routes.models import Route


class Trip(models.Model):
    name = models.CharField(max_length=100)
    popularity = models.CharField(max_length=100)
    occupancy = models.CharField(max_length=100)
    profitability = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
