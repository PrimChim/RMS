from django.shortcuts import render
from .models import MenuItems

# Create your views here.

def menu(request):
    menu = MenuItems.objects.all()
    return render(request, 'menu.html', {'menu': menu})

def add_items(request):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        menu = MenuItems.objects.create(name=name, price=price, description=description)
        menu.save()
        return render(request, 'add-items.html', {'message': 'Item added successfully'})
    return render(request, 'add-items.html')