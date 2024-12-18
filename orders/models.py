from django.db import models
from menu.models import MenuItems

# Create your models here.

class Orders(models.Model):
    table_number =  models.IntegerField(default=2)
    status = models.CharField(max_length=1, choices={
        "C": "Complete",
        "P": "Pending",
        "R": "Received",
    }, default="R")

    def __str__(self):
        return str(self.id)

class OrderItems(models.Model):
    order_number = models.ForeignKey(Orders, on_delete=models.CASCADE)
    name = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.order_number)