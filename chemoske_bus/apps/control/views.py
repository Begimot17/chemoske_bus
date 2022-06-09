from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from flights.models import Trip
from tickets.models import Ticket
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

def index(request,id):
    trip = Trip.objects.get(id=id)

    try:
        a = Control.objects.get(trip=trip)
        on=0
        off=0
        all=0
        for x in a.num_seat.all():
            if x.status=='on':
                on+=1
            elif x.status=='off':
                off+=1
            all+=1
        config = {
            'control': a,
            'on': on,
            'off': off,
            'all': all
        }
        return render(request, 'control/index.html', config)
    except ObjectDoesNotExist:
        fleets = Fleet.objects.all()
        config = {
            'trip': trip,
            'fleets':fleets
        }
        return render(request, 'control/add.html', config)


def reg(request,id):
    profile = Control.objects.create(trip = Trip.objects.get(id=id),
                                        fleet = Fleet.objects.get(id=request.POST['fleet']),
                                        depar_time = datetime.strptime(request.POST['depar_time'], "%Y-%m-%dT%H:%M"),
                                        arrival_time = datetime.strptime(request.POST['arrival_time'], "%Y-%m-%dT%H:%M"),
                                        degree_of_comf = request.POST['degree_of_comf'],
                                        num_of_custom = request.POST['num_of_custom']
                                   )

    for x in range(Fleet.objects.get(id=request.POST['fleet']).driver_1.bus.num_of_seat):
        seat=Seat.objects.create(name=x+1,status='off')
        profile.num_seat.add(seat)
    profile.save()
    return HttpResponseRedirect('/control/%s' % profile.trip.id)
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
    return render(request, 'control/update.html',config)
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
    return HttpResponseRedirect(reverse('control:index'))
def delete(request, id):
    Fleet.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('control:index'))

def buy(request, id):
    control = Control.objects.get(id=id)
    seat = Seat.objects.get(id=request.POST['seat'])
    config = {
        'control': control,
        'seat': seat
    }
    return render(request, 'control/buy.html', config)


def add_ticket(request, id):
    control = Control.objects.get(id=id)
    seat = Seat.objects.get(id=request.POST.get('seat', None))
    seat.status='on'
    seat.save()
    ticket = Ticket.objects.create(seat=seat,
                                   control=control,
                                   client_name=request.POST['client_name'],
                                   contact_info=request.POST['contact_info']
                                     )
    ticket.save()
    return HttpResponseRedirect(reverse('tickets:index'))