from django.db import models


class Place(models.Model):
    name=models.CharField(max_length=100)


class Route(models.Model):
    arrival = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='arrival')
    departure = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='departure')

