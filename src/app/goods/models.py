from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='goods_images', null=True, blank=True)
    price = models.DecimalField(default = 0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default = 0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(default = 0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.name
    
    def display_id(self):
        return f'{self.id:05d}'
    
    def calculate_discount(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

