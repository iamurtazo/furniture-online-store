from django.urls import path
from orders.views import CreateOrderView, OrderDetailView

app_name = 'orders'

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='create_order'),
    path('order_detail/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
]