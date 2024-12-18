from django.contrib import admin
from .models import *

# Register your models here.

class MenuItemsAdmin(admin.ModelAdmin):
    list_display = "id", "name", "price", "description",

admin.site.register(MenuItems, MenuItemsAdmin)