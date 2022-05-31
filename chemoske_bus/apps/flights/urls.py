from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('',views.index, name='index'),
path('add/', views.add, name='add'),
    path('reg/', views.reg, name='reg'),
path('delete/<int:id>', views.delete, name='delete'),
]
