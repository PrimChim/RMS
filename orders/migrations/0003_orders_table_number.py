# Generated by Django 5.0.6 on 2024-12-17 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orders_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='table_number',
            field=models.IntegerField(default=2),
        ),
    ]
