from django.shortcuts import render
from django.http import HttpResponse
from menu.models import MenuItems
from .models import *

# Create your views here.

def create_orders(request):
    if request.method == "POST":
        table_number = request.POST.get('table-number')
        items = request.POST.getlist('items[]')
        quantities = request.POST.getlist('quantity[]')
        order = Orders.objects.create(table_number=table_number)
        order.save()
        if order is not None:
            for i in range(len(items)):
                item = int(items[i])
                quantity = int(quantities[i])
                order_item = OrderItems.objects.create(order_number=order, name=MenuItems.objects.get(id=item), quantity=quantity)
                order_item.save()
    items = MenuItems.objects.all()
    return render(request, 'orders/create_orders.html',{"items": items})

def kot(request):
    # Fetch all orders
    orders = Orders.objects.all()

    # Construct a list of orders with their items
    order_details = []
    for order in orders:
        # Get all order items related to the current order
        items = OrderItems.objects.filter(order_number=order)
        
        # Append order and its items to the details list
        order_details.append({
            'order': order,
            'items': [
                {
                    'name': item.name.name,  # Access MenuItem name
                    'quantity': item.quantity,
                }
                for item in items
            ]
        })

    # Send data to the template
    return render(request, 'orders/kot.html', {'order_details': order_details})