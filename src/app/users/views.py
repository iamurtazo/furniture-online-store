from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from users.forms import UserLoginForm, UserRegistrationForm

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
        # Update user profile
        user = request.user
        new_username = request.POST.get('username', '').strip()
        
        # Validate username changes
        if new_username and new_username != user.username:
            # Check if username already exists
            from django.contrib.auth import get_user_model
            User = get_user_model()
            if User.objects.filter(username=new_username).exclude(pk=user.pk).exists():
                messages.error(request, f'Username "{new_username}" is already taken. Please choose a different one.')
                return redirect('users:profile')
        
        # Update user fields
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        if new_username:
            user.username = new_username
        
        try:
            user.save()
            success_msg = 'Profile updated successfully!'
            if new_username and new_username != request.POST.get('old_username', ''):
                success_msg = f'Profile updated successfully! Your username is now "{new_username}".'
            messages.success(request, success_msg)
        except Exception as e:
            messages.error(request, 'Error updating profile. Please try again.')
        
        return redirect('users:profile')
    
    context = {
        'title': 'Home - Profile'
    }
    
    return render(request, 'users/profile.html', context)