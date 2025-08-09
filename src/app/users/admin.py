from django.contrib import admin

from carts.admin import CartTabAdmin
from .models import Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email' ]
    search_fields = ['first_name', 'last_name', 'email']
    
    inlines = [CartTabAdmin]
   
