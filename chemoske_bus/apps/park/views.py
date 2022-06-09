from django.shortcuts import render
from .models import *
from datetime import date
from drivers.models import Driver
from flights.models import Trip
from routes.models import Route
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
    c = Trip.objects.all()
    config = {
        'drivers': a,
        'routes': b,
        'trips': c
    }
    return render(request, 'park/add.html', config)


def reg(request):
    profile = Fleet.objects.create(number=request.POST['number'],
                                   driver_1=Driver.objects.get(id=request.POST['driver_1']),
                                   driver_2=Driver.objects.get(id=request.POST['driver_2']),
                                   route=Route.objects.get(id=request.POST['route']),
                                   mileage=request.POST['mileage'],
                                   num_of_flights_perform=request.POST['num_of_flights_perform'],
                                   date_of_next=request.POST['depar_time'],
                                   date_of_last=request.POST['arrival_time'],
                                   current_flight=Trip.objects.get(id=request.POST['current_flight'])
                                   )
    profile.save()
    return HttpResponseRedirect(reverse('park:index'))
def update(request,id):
    fleet=Fleet.objects.get(id=id)
    a = Driver.objects.all()
    b = Route.objects.all()
    c = Trip.objects.all()
    config = {
        'fleet': fleet,
        'drivers': a,
        'routes': b,
        'trips': c
    }
    return render(request, 'park/update.html',config)
def upd(request,id):
    fleet = Fleet.objects.get(id=id)
    fleet.number = request.POST['number']
    fleet.driver_1 = Driver.objects.get(id=request.POST['driver_1'])
    fleet.driver_2 = Driver.objects.get(id=request.POST['driver_2'])
    fleet.route = Route.objects.get(id=request.POST['route'])
    fleet.mileage = request.POST['mileage']
    fleet.num_of_flights_perform = request.POST['num_of_flights_perform']
    fleet.date_of_next = request.POST['depar_time']
    fleet.date_of_last = request.POST['arrival_time']
    fleet.current_flight = Trip.objects.get(id=request.POST['current_flight'])
    fleet.save()
    return HttpResponseRedirect(reverse('park:index'))
def delete(request, id):
    Fleet.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('park:index'))
