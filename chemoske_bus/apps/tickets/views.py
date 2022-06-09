from django.shortcuts import render
from .models import *
from park.models import *
from control.models import *
from flights.models import *
from datetime import date
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    a = Ticket.objects.all()
    c = Control.objects.all()
    config = {
        'tickets': a,
        'controls': c
    }
    return render(request, 'tickets/index.html', config)


def search(request):
    a = Control.objects.get(id=request.POST['control'])
    b = Ticket.objects.filter(control=a)
    c = Control.objects.all()
    config = {
        'tickets': b,
        'controls': c
    }
    return render(request, 'tickets/index.html', config)
