from django.shortcuts import render
from .models import *
from park.models import *
from flights.models import *
from datetime import date
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    a = Ticket.objects.all()
    config = {
        'tickets': a
    }
    return render(request, 'tickets/index.html',config)


def add(request):
    a = Trip.objects.all()
    b = Fleet.objects.all()
    config = {
        'trips': a,
        'fleets': b
    }
    return render(request, 'tickets/add.html',config)

def reg(request):
    profile = Ticket.objects.create( name=request.POST['name'],
                                     num_seat=request.POST['num_seat'],
                                     contact_info=request.POST['contact_info'],
                                     trip= Trip.objects.get(id=request.POST['trip']),
                                     fleet=Fleet.objects.get(id=request.POST['fleet']),
                                     depar_time=request.POST['depar_time'],
                                     arrival_time=request.POST['arrival_time'],
                                     price=request.POST['price'],
                                     degree_of_comf=request.POST['degree_of_comf'],
                                     num_of_custom=request.POST['num_of_custom']
                                     )
    profile.save()
    return HttpResponseRedirect(reverse('tickets:index'))
def update(request,id):
    ticket=Ticket.objects.get(id=id)
    a = Trip.objects.all()
    b = Fleet.objects.all()
    config = {
        'trips': a,
        'fleets': b,
        'ticket':ticket
    }
    return render(request, 'tickets/update.html',config)
def upd(request,id):
    ticket = Ticket.objects.get(id=id)
    ticket.name=request.POST['name']
    ticket.num_seat = request.POST['num_seat']
    ticket.contact_info = request.POST['contact_info']
    ticket.trip = Trip.objects.get(id=request.POST['trip'])
    ticket.fleet = Fleet.objects.get(id=request.POST['fleet'])
    ticket.depar_time = request.POST['depar_time']
    ticket.arrival_time = request.POST['arrival_time']
    ticket.price = request.POST['price']
    ticket.degree_of_comf = request.POST['degree_of_comf']
    ticket.num_of_custom = request.POST['num_of_custom']
    ticket.save()
    return HttpResponseRedirect(reverse('tickets:index'))
def delete(request, id):
    Ticket.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('tickets:index'))