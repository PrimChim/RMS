from django.urls import path
from .views import *

app_name = 'orders'
urlpatterns = [
    path('create-orders', create_orders,name='create-orders'),
    path('kot',kot,name='kot'),
]