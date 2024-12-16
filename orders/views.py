from django.shortcuts import render
from django.http import HttpResponse
from menu.models import MenuItems

# Create your views here.

def create_orders(request):
    items = MenuItems.objects.all()
    return render(request, 'orders/create_orders.html',{"items": items})