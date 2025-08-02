from django import forms
from users.models import Users
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField(
        widget=forms.TextInput
        (
            attrs =
            {
                "autofocus": True,
                "class": "form-control", 
                "placeholder": "username"
            }
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput
        (
            attrs =
            {
                "autocomplete": "current-password",
                "class": "form-control", 
                "placeholder": "password"
            }
        )
    )

    class Meta:
        model = Users
        fields: list[str] = ['username', 'password']

        
        
