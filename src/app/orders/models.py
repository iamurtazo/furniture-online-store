from typing import Iterable
from django.db import models
from users.models import Users
from goods.models import Products
from django.urls import reverse

# Create your models here.

class OrderItemQuerySet(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    
class Order(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    requires_delivery = models.BooleanField(default=False)
    delivery_address = models.TextField(max_length=255, null=True, blank=True)
    payment_on_get = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=255, default = 'In Progress')
    
    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        
    def __str__(self):
        return f'Order {self.id} by {self.user.username}'
    
    def get_absolute_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.pk})
    
    def get_total_quantity(self):
        return sum(item.quantity for item in self.orderitem_set.all())
    
    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.orderitem_set.all())
    
    def display_id(self):
        return f'{self.id:05d}'
    
    def get_status_badge_class(self):
        status_classes = {
            'In Progress': 'bg-warning text-dark',
            'Processing': 'bg-info text-white',
            'Shipped': 'bg-primary text-white',
            'Delivered': 'bg-success text-white',
            'Cancelled': 'bg-danger text-white',
        }
        return status_classes.get(self.status, 'bg-secondary text-white')
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.SET_DEFAULT, null=True, default=None)
    name = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'order_item'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
        
    objects = OrderItemQuerySet.as_manager()
        
    def products_price(self):
        return round(self.product.price * self.quantity, 2)
    
    def __str__(self):
        return f'Item: {self.name} | Order No: {self.order.pk}'