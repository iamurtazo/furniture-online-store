from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from carts.merge_utils import merge_carts
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from orders.models import Order, OrderItem

# Create your views here.

def login(request):
    
    if request.method == 'POST':    
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            
            session_key = request.session.session_key
            
            if user:
                auth.login(request, user)
                welcome_name = user.first_name or user.username
                messages.success(request, f'Welcome back, {welcome_name}! You have successfully logged in.')
                
                # Merge anonymous cart with user's existing cart
                if session_key:
                    merged_items = merge_carts(user, session_key)
                    if merged_items > 0:
                        messages.info(request, f'{merged_items} item(s) from your cart have been saved.')
                        
                return redirect('main:index')
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'Home - Authorization',
        'form': form
    }
    
    return render(request, 'users/login.html', context)
@login_required
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
            
            # Transfer anonymous cart to the new user
            if request.session.session_key:
                merged_items = merge_carts(user, request.session.session_key)
                if merged_items > 0:
                    messages.info(request, f'{merged_items} item(s) have been added to your cart.')
                    
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
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            # Check what changed
            old_username = request.user.username
            new_username = form.cleaned_data.get('username')
            image_changed = 'image' in request.FILES
            
            # Save the form
            user = form.save()
            
            # Provide appropriate success message
            success_parts = []
            if old_username != new_username:
                success_parts.append(f'username updated to "{new_username}"')
            if image_changed:
                success_parts.append('profile photo updated')
            
            if success_parts:
                message = f'Profile updated successfully! {", ".join(success_parts).capitalize()}.'
            else:
                message = 'Profile updated successfully!'
            
            messages.success(request, message)
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
    
    # Get user's orders with related items
    orders = Order.objects.filter(user=request.user).prefetch_related(
        'orderitem_set__product'
    ).order_by('-created_at')
    
    context = {
        'title': 'Home - Profile',
        'form': form,
        'orders': orders,
    }
    
    return render(request, 'users/profile.html', context)

@login_required
def users_cart(request):
    return render(request, 'users/users_cart.html')