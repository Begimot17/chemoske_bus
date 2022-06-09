from django.urls import path
from . import views

app_name = 'control'

urlpatterns = [
    path('<int:id>',views.index, name='index'),
    path('reg/<int:id>', views.reg, name='reg'),
    path('update/<int:id>', views.update, name='update'),
    path('upd/<int:id>', views.upd, name='upd'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('buy/<int:id>', views.buy, name='buy'),
    path('add_ticket/<int:id>', views.add_ticket, name='add_ticket'),
]
