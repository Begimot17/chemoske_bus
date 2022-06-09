from django.db import models
from control.models import *


class Ticket(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    control = models.ForeignKey(Control, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
