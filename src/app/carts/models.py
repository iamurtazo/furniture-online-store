from django.db import models
from users.models import Users
from goods.models import Products

class CartQuerySet(models.QuerySet):
    
    def total_price(self):
        """
        Calculate the total price of all items in the cart.
        
        This method iterates through all Cart objects in the queryset
        and sums up the total price for each item by calling the
        products_price() method on each Cart instance.
        
        Returns:
            float: The total price of all cart items combined
        """
        return sum(item.products_price() for item in self)
    
    def total_quantity(self):
        """
        Calculate the total quantity of all items in the cart.
        
        This method iterates through all Cart objects in the queryset
        and sums up the total quantity for each item.
        
        Returns:
            int: The total quantity of all cart items combined
        """
        if self:
            return sum(item.quantity for item in self)
        return 0
    
    
    
    
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        
    objects = CartQuerySet.as_manager()
        
    def __str__(self):
        return f'Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'

    def products_price(self):
        return round(self.product.get_discounted_price() * self.quantity, 2)
    
    
