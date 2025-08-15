from django.urls import path
from .views import IndexView, AboutView, DeliveryPaymentView, ContactInfoView
from django.views.decorators.cache import cache_page

app_name = 'main'

urlpatterns = [
    path('', cache_page(60)(IndexView.as_view()), name='index'),
    path('about/', cache_page(60)(AboutView.as_view()), name='about'),
    path('delivery-payment/', DeliveryPaymentView.as_view(), name='delivery_payment'),
    path('contact/', ContactInfoView.as_view(), name='contact_info'),
]