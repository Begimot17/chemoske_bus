from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    a = Driver.objects.all()
    config = {
        'drivers': a
    }
    return render(request, 'drivers/index.html',config)


def add(request):
    a = Bus.objects.all()
    config = {
        'buses': a
    }
    return render(request, 'drivers/add.html',config)

def reg(request):
    profile = Driver.objects.create(name=request.POST['name'],
                                     category=request.POST['category'],
                                     experience=request.POST['experience'],
                                     num_of_fines=0,
                                     num_of_flights=0,
                                     salary=request.POST['salary'],
                                     degree_of_cong=request.POST['degree_of_cong'],
                                     degree_of_reliab=request.POST['degree_of_reliab'],
                                     bus= Bus.objects.get(id=request.POST['bus'])
                                     )
    profile.save()
    return HttpResponseRedirect(reverse('drivers:index'))

