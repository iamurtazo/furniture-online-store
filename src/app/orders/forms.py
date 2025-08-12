from django import forms
from .models import Order

class CreateOrderForm(forms.ModelForm):
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField()
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField()
    
    
    # first_name = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        
    # )
    
    # last_name = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    # )
    
    # email = forms.EmailField(
    #     widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    # )
    
    # phone_number = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
    # )
    
    # requires_delivery = forms.BooleanField(
    #     widget=forms.RadioSelect(),
    #     choices=[(1, 'Yes'), (0, 'No')],
    #     initial=0,
    # )
    
    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(attrs={
    #         'class': 'form-control', 
    #         'id': 'delivery_address', 
    #         'placeholder': 'Delivery Address',
    #         'rows': 2,
    #         }
    #     ),
    # )
    
    # payment_on_get = forms.BooleanField(
    #     widget=forms.RadioSelect(),
    #     choices=[(1, 'Yes'), (0, 'No')],
    #     initial=0,
    # )
    
    
    
   
        
        