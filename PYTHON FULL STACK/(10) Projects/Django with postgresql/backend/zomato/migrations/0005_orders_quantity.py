# Generated by Django 5.1.2 on 2024-10-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0004_remove_products_orders_orders_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]