from django.shortcuts import render
from .models import *
from datetime import date
from drivers.models import *
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    a = Fleet.objects.all()
    config = {
        'parks': a
    }
    return render(request, 'park/index.html', config)


def add(request):
    a = Driver.objects.all()
    b = Route.objects.all()
    config = {
        'drivers': a,
        'routes': b
    }
    return render(request, 'park/add.html', config)


def reg(request):
    profile = Fleet.objects.create(number=request.POST['number'],
                                   driver_1=Driver.objects.get(id=request.POST['driver_1']),
                                   driver_2=Driver.objects.get(id=request.POST['driver_2']),
                                   route=Route.objects.get(id=request.POST['route']),
                                   mileage=request.POST['mileage'],
                                   num_of_flights_perform=1,
                                   date_of_next=date.today(),
                                   date_of_last=date.today(),
                                   current_flight=1,
                                   )
    profile.save()
    return HttpResponseRedirect(reverse('park:index'))
