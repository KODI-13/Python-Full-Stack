from django.db import models

# Create your models here.
class Customers(models.Model):
    cust_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cust_name


#2nd step for above two steps
class Orders(models.Model):
    ord_date = models.DateField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - {self.customer}"


class Products(models.Model):
    p_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.p_name


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product} in Order {self.order}"
    
    @property
    def total_price(self):
        return self.quantity * self.product.price









