from django.urls import path
from . import views

app_name = 'park'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('reg/', views.reg, name='reg'),
]
