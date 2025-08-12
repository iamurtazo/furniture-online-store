from django.urls import path
from orders.views import *

app_name = 'orders'

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
]