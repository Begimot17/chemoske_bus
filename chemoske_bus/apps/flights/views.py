from .models import *
from routes.models import *
from datetime import date
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    b = Trip.objects.all()
    config = {
        'trips': b
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
                                  occupancy=request.POST['occupancy'],
                                     profitability=request.POST['profitability'],
                                     route=Route.objects.get(id=request.POST['route'])
                                     )
    profile.save()
    return HttpResponseRedirect(reverse('flights:index'))

def delete(request, id):
    Trip.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('flights:index'))