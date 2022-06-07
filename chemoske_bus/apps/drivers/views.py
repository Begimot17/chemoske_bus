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
    return render(request, 'drivers/index.html', config)


def add(request):
    a = Bus.objects.all()
    config = {
        'buses': a
    }
    return render(request, 'drivers/add.html', config)


def reg(request):
    profile = Driver.objects.create(name=request.POST['name'],
                                    category=request.POST['category'],
                                    experience=request.POST['experience'],
                                    num_of_fines=request.POST['num_of_fines'],
                                    num_of_flights=request.POST['num_of_flights'],
                                    salary=request.POST['salary'],
                                    degree_of_cong=request.POST['degree_of_cong'],
                                    degree_of_reliab=request.POST['degree_of_reliab'],
                                    bus=Bus.objects.get(id=request.POST['bus'])
                                    )
    profile.save()
    return HttpResponseRedirect(reverse('drivers:index'))


def update(request, id):
    driver = Driver.objects.get(id=id)
    a = Bus.objects.all()
    config = {
        'buses': a,
        'driver': driver
    }
    return render(request, 'drivers/update.html', config)


def upd(request, id):
    driver = Driver.objects.get(id=id)
    driver.name = request.POST['name']
    driver.category = request.POST['category']
    driver.experience = request.POST['experience']
    driver.num_of_fines = request.POST['num_of_fines']
    driver.num_of_flights = request.POST['num_of_flights']
    driver.salary = request.POST['salary']
    driver.degree_of_cong = request.POST['degree_of_cong']
    driver.degree_of_reliab = request.POST['degree_of_reliab']
    driver.bus = Bus.objects.get(id=request.POST['bus'])
    driver.save()
    return HttpResponseRedirect(reverse('drivers:index'))


def delete(request, id):
    Driver.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('drivers:index'))
