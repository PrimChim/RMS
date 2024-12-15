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
    list_display = "id","name","quantity","status",
    ordering = "id",
    actions = make_completed, make_pending,

admin.site.register(Orders, OrdersAdmin)