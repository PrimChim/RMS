from django.urls import path
from .views import *

app_name = 'menu'
urlpatterns = [
    path('', menu, name='menu'),
    path('add-items',add_items,name='add-items'),
    path('edit-items/<int:id>',edit_menu_item,name='edit-item'),
    path('delete-items/<int:id>',delete_menu_item,name='delete-item'),
]
