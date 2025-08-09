from django.contrib import admin
from carts.models import Cart

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'created_at'
    search_fields = 'product', 'quantity', 'created_at'
    readonly_fields = ('created_at',)
    extra = 1
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'quantity', 'created_at']
    search_fields = ['user', 'product', 'quantity', 'created_at']
    
    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Anonymous'
    
    def product_display(self, obj):
        return str(obj.product.name)
    
    # user_display.short_description = 'User'
    # product_display.short_description = 'Product'
    
    
    

# admin.site.register(Cart, CartAdmin)