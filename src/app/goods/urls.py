from django.urls import path
from .views import *

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/', catalog, name='index'),
    path('<slug:category_slug>/<int:page_number>/', catalog, name='page'),
    path('product/<int:product_id>', product, name='product'),
    # path('product/<slug:product_slug>', product, name='product'),
]