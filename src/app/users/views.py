from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

# Create your views here.

def login(request):
    
    if request.method == 'POST':    
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                welcome_name = user.first_name or user.username
                messages.success(request, f'Welcome back, {welcome_name}! You have successfully logged in.')
                return redirect('main:index')
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'Home - Authorization',
        'form': form
    }
    
    return render(request, 'users/login.html', context)

def logout(request):
    if request.user.is_authenticated:
        username = request.user.first_name or request.user.username
        auth.logout(request)
        messages.success(request, f'Goodbye {username}! You have been successfully logged out.')
    
    context = {
        'title': 'Home - Logout'
    }
    
    return render(request, 'users/logout.html', context)

def registration(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created successfully for {user.username}! You can now log in.')
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Home - Registration',
        'form': form
    }

    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            # Check if username changed
            old_username = request.user.username
            new_username = form.cleaned_data.get('username')
            
            # Save the form
            user = form.save()
            
            # Provide appropriate success message
            if old_username != new_username:
                messages.success(request, f'Profile updated successfully! Your username is now "{new_username}".')
            else:
                messages.success(request, 'Profile updated successfully!')
            
            return redirect('users:profile')
        else:
            # Form has validation errors - they'll be displayed in the template
            context = {
                'title': 'Home - Profile',
                'form': form
            }
            return render(request, 'users/profile.html', context)
    else:
        # GET request - create form with current user data
        form = UserProfileForm(instance=request.user)
    
    context = {
        'title': 'Home - Profile',
        'form': form
    }
    
    return render(request, 'users/profile.html', context)