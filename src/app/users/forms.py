from django import forms
from users.models import Users
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

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
            # "placeholder": "Enter your first name"
        })
    )
    
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            # "placeholder": "Enter your last name"
        })
    )
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True, 
            "class": "form-control", 
            # "placeholder": "Enter your username"
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control", 
            # "placeholder": "Enter your email"
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password", 
            "class": "form-control", 
            # "placeholder": "Enter password"
        })
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password", 
            "class": "form-control", 
            # "placeholder": "Confirm password"
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


class UserProfileForm(UserChangeForm):
    """
    Form for updating user profile information.
    Inherits from UserChangeForm following Django best practices.
    """
    
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            # "placeholder": "Enter your first name"
        }),
        required=True
    )
    
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            # "placeholder": "Enter your last name"
        }),
        required=True
    )
    
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            # "placeholder": "Enter your username"
        }),
        required=True,
        help_text="Choose a unique username. This will be your login identifier."
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control", 
            # "placeholder": "Enter your email"
        }),
        required=True
    )
    
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            "class": "form-control",
            "accept": "image/*"
        }),
        required=False,
        help_text="Upload a profile picture (JPG, PNG, GIF - Max 5MB)"
    )
    
    # Remove password field from profile editing
    password = None
    
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove password field completely
        if 'password' in self.fields:
            del self.fields['password']
    
    def clean_username(self):
        """
        Validate username for uniqueness and format.
        """
        username = self.cleaned_data.get('username')
        
        if not username:
            raise forms.ValidationError("Username is required.")
        
        # Check minimum length
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        
        # Check format (letters, numbers, underscores only)
        import re
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise forms.ValidationError("Username can only contain letters, numbers, and underscores.")
        
        # Check uniqueness (exclude current user)
        if self.instance and self.instance.pk:
            if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(f'Username "{username}" is already taken. Please choose a different one.')
        else:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(f'Username "{username}" is already taken. Please choose a different one.')
        
        return username
    
    def clean_email(self):
        """
        Validate email for format and uniqueness.
        """
        email = self.cleaned_data.get('email')
        
        if not email:
            raise forms.ValidationError("Email is required.")
        
        # Check uniqueness (exclude current user)
        if self.instance and self.instance.pk:
            if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(f'Email "{email}" is already registered. Please use a different email.')
        else:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(f'Email "{email}" is already registered. Please use a different email.')
        
        return email
    
    def clean_image(self):
        """
        Validate uploaded image for size and format.
        """
        image = self.cleaned_data.get('image')
        
        if image:
            # Check file size (5MB limit)
            if image.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise forms.ValidationError("Image file too large. Please keep it under 5MB.")
            
            # Check file type
            valid_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif']
            if hasattr(image, 'content_type') and image.content_type not in valid_types:
                raise forms.ValidationError("Invalid image format. Please use JPG, PNG, or GIF.")
        
        return image
