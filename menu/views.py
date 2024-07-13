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

def edit_menu_item(request, id):
    menu = MenuItems.objects.get(id=id)
    if request.method == "POST":
        menu.name = request.POST['name']
        menu.price = request.POST['price']
        menu.description = request.POST['description']
        menu.save()
        return render(request, 'edit-item.html', {'message': 'Item updated successfully'})
    return render(request, 'edit-item.html', {'item': menu})

def delete_menu_item(request, id):
    item = MenuItems.objects.get(id=id)
    item.delete()
    menu = MenuItems.objects.all()
    return render(request, 'menu.html', {'message': 'Item deleted successfully', 'menu': menu})