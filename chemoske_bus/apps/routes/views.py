from django.shortcuts import render
from .models import *
from datetime import date
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    a = Route.objects.all()
    config = {
        'routes': a
    }
    return render(request, 'routes/index.html',config)
def add(request):
    a = Place.objects.all()
    config = {
        'places': a
    }
    return render(request, 'routes/add.html',config)

def reg(request):
    route = Route.objects.create(photo=request.POST['photo'],
                                     name=request.POST['name'],
                                     arrival= Place.objects.get(id=request.POST['arrival']),
                                     departure=Place.objects.get(id=request.POST['departure'])
                                     )
    route.save()
    return HttpResponseRedirect(reverse('routes:index'))
def update(request,id):
    route=Route.objects.get(id=id)
    a = Place.objects.all()
    config = {
        'route': route,
        'places': a
    }
    return render(request, 'routes/update.html',config)
def upd(request,id):
    route = Route.objects.get(id=id)
    route.photo=request.POST['photo']
    route.name = request.POST['name']
    route.arrival = Place.objects.get(id=request.POST['arrival'])
    route.departure = Place.objects.get(id=request.POST['departure'])
    route.save()
    return HttpResponseRedirect(reverse('routes:index'))
def delete(request, id):
    Route.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('routes:index'))
