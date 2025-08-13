from django import forms
import re
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
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        
        if not phone_number:
            raise forms.ValidationError("Phone number is required.")
        
        # Remove all whitespace
        phone_number = phone_number.strip()
        
        # Define allowed characters for phone numbers
        # Digits, plus sign, hyphens, spaces, parentheses, dots
        allowed_chars_pattern = re.compile(r'^[+\d\s\-\(\)\.\s]+$')
        
        if not allowed_chars_pattern.match(phone_number):
            raise forms.ValidationError(
                "Phone number can only contain digits, spaces, hyphens (-), "
                "parentheses (), dots (.), and plus sign (+)"
            )
        
        # Clean the phone number by removing non-digit characters except +
        cleaned_number = re.sub(r'[^\d+]', '', phone_number)
        
        # Validate international phone number formats
        international_patterns = [
            # International format with country code (+1234567890 to +123456789012345)
            r'^\+\d{7,15}$',
            # US/Canada format (10 digits)
            r'^\d{10}$',
            # Many international formats (7-15 digits without +)
            r'^\d{7,15}$',
        ]
        
        # Check if cleaned number matches any valid pattern
        is_valid = any(re.match(pattern, cleaned_number) for pattern in international_patterns)
        
        if not is_valid:
            raise forms.ValidationError(
                "Please enter a valid phone number. Examples: "
                "+1234567890, +998901234567, 1234567890, (123) 456-7890"
            )
        
        # Additional validation for specific formats
        if cleaned_number.startswith('+'):
            # International format: must have at least 7 digits after +
            digits_after_plus = cleaned_number[1:]
            if len(digits_after_plus) < 7:
                raise forms.ValidationError(
                    "International phone number must have at least 7 digits after country code."
                )
        else:
            # Domestic format: check for common lengths
            if len(cleaned_number) < 7:
                raise forms.ValidationError(
                    "Phone number must be at least 7 digits long."
                )
        
        # Store the cleaned version for saving
        return cleaned_number
    
    
        