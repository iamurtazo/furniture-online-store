from django import forms
from .models import Order

class CreateOrderForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.BooleanField(required=False)
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.BooleanField(required=False)
    
    class Meta:
        model = Order
        fields = ('phone_number', 'requires_delivery', 'delivery_address', 'payment_on_get')
        