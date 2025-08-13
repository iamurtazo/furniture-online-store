from django.urls import path
from .views import IndexView, AboutView, DeliveryPaymentView, ContactInfoView

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('delivery-payment/', DeliveryPaymentView.as_view(), name='delivery_payment'),
    path('contact/', ContactInfoView.as_view(), name='contact_info'),
]