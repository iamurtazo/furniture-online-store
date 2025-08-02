from django import forms
from users.models import Users
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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

class UserRegistrationForm(UserCreationForm):
    
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            "placeholder": "Enter your first name"
        })
    )
    
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            "placeholder": "Enter your last name"
        })
    )
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True, 
            "class": "form-control", 
            "placeholder": "Enter your username"
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control", 
            "placeholder": "Enter your email"
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password", 
            "class": "form-control", 
            "placeholder": "Enter password"
        })
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password", 
            "class": "form-control", 
            "placeholder": "Confirm password"
        })
    )
    
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Users.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email
