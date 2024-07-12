from django.urls import path
from .views import *

app_name = 'menu'
urlpatterns = [
    path('', menu, name='menu'),
    path('add-items',add_items,name='add-items')
]
