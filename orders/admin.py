from django.contrib import admin
from .models import *

# Register your models here.

@admin.action(description="Make selected as completed")
def make_completed(modeladmin, request, queryset):
    queryset.update(status="C")

@admin.action(description="Make selected as pending")
def make_pending(modeladmin, request, queryset):
    queryset.update(status="P")

class OrdersAdmin(admin.ModelAdmin):
    list_display = "id", "table_number","status",
    ordering = "id",
    actions = make_completed, make_pending,

admin.site.register(Orders, OrdersAdmin)

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = "id", "order_number", "name", "quantity",
    ordering = "id",

admin.site.register(OrderItems, OrderItemsAdmin)