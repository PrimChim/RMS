from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def create_orders(request):
    return HttpResponse("orders page")