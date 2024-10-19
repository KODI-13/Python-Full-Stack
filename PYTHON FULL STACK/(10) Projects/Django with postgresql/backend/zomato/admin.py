from django.contrib import admin
from zomato.models import Customers, Orders, Products, OrderItem

# Register your models here.
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['id', 'cust_name']

admin.site.register(Customers, CustomersAdmin)



class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'ord_date', 'customer']
    
admin.site.register(Orders, OrdersAdmin)


# if used 2nd way of many to many field
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_name', 'price']

admin.site.register(Products, ProductsAdmin)




class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']

admin.site.register(OrderItem, OrderItemAdmin)
