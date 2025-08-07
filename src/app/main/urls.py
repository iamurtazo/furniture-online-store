from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('delivery-payment/', delivery_payment, name='delivery_payment'),
    path('contact/', contact_info, name='contact_info'),
]