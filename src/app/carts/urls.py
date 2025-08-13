from django.urls import path
from carts.views import CartAddView, cart_change, cart_remove

app_name = 'carts'

urlpatterns = [
    path('cart_add/', CartAddView.as_view(), name='cart_add'),
    path('cart_change/', cart_change, name='cart_change'),
    path('cart_remove/', cart_remove, name='cart_remove'),
]