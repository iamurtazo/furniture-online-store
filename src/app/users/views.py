from django.shortcuts import render

# Create your views here.

def login(request):
    
    context = {
        'title': 'Home - Authorization'
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