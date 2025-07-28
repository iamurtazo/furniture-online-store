from django.urls import path
from .views import *

app_name = 'goods'

urlpatterns = [
    path('', catalog, name='index'),
    path('product/<int:product_id>', product, name='product'),
    # path('product/<slug:product_slug>', product, name='product'),
]