from .models import *
from control.models import *
from routes.models import *
from datetime import date
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    b = Trip.objects.all()
    c = Control.objects.all()
    config = {
        'trips': b,
        'controls': c
    }
    return render(request, 'flights/index.html',config)

def search(request):
    a = Control.objects.get(id=request.POST['control'])
    b = Trip.objects.all(control=a)
    c = Control.objects.all()
    config = {
        'trips': b,
        'controls': c
    }
    return render(request, 'flights/index.html',config)

def add(request):
    b = Route.objects.all()
    config = {
        'routes': b
    }
    return render(request, 'flights/add.html',config)

def reg(request):
    profile = Trip.objects.create(photo=request.POST['photo'],
                                     name=request.POST['name'],
                                  price=request.POST['price'],
                                  popularity=request.POST['popularity'],
                                     profitability=request.POST['profitability'],
                                     route=Route.objects.get(id=request.POST['route'])
                                     )
    profile.save()
    return HttpResponseRedirect(reverse('flights:index'))
def update(request,id):
    trip=Trip.objects.get(id=id)
    a = Route.objects.all()
    config = {
        'routes': a,
        'trip': trip
    }
    return render(request, 'flights/update.html',config)
def upd(request,id):
    trip = Trip.objects.get(id=id)
    trip.name = request.POST['name']
    trip.photo=request.POST['photo']
    trip.price = request.POST['price']
    trip.popularity = request.POST['popularity']
    trip.profitability = request.POST['profitability']
    trip.route = Route.objects.get(id=request.POST['route'])
    trip.save()
    return HttpResponseRedirect(reverse('flights:index'))
def delete(request, id):
    Trip.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('flights:index'))