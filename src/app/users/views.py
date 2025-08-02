from django.shortcuts import render, redirect
from django.contrib import auth
from users.forms import UserLoginForm

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
                return redirect('main:index')
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'Home - Authorization',
        'form': form
    }
    
    return render(request, 'users/login.html', context)

def logout(request):
    
    context = {
        'title': 'Home - Logout'
    }
    
    return render(request, 'users/logout.html', context)

def registration(request):
    
    context = {
        'title': 'Home - Registration'
    }
    
    return render(request, 'users/registration.html', context)

def profile(request):
    
    context = {
        'title': 'Home - Profile'
    }
    
    return render(request, 'users/profile.html', context)