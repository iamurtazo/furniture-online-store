from django.urls import path
from goods.views import *

app_name = 'goods'

urlpatterns = [
    path('search/', catalog, name='search'),
    path('<slug:category_slug>/', catalog, name='index'),
    path('product/<int:product_id>', product, name='product'),
]