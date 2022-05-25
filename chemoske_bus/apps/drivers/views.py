from django.shortcuts import render

def index(request):
    return render(request, 'drivers/index.html')
def add(request):
    return render(request, 'drivers/add.html')

