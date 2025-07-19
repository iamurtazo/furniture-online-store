from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
# admin.site.register(Categories, CategoriesAdmin)
# admin.site.register(Products, ProductsAdmin)
