from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    user= models.ForeignKey(User, on_delete=models.CASCADE)