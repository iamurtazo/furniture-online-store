from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from carts.models import Cart
from carts.merge_utils import merge_carts
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from orders.models import Order, OrderItem

# Create your views here.

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('main:index')
    
    def get_context_data(self, **kwargs):
        """Add custom context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Authorization'
        return context
    
    def form_valid(self, form):
        """Handle successful login with cart merging."""
        # Store session key before login (it changes after login)
        session_key = self.request.session.session_key
        
        # Perform the login
        response = super().form_valid(form)
        
        # Get the logged-in user
        user = self.request.user
        welcome_name = user.first_name or user.username
        messages.success(
            self.request, 
            f'Welcome back, {welcome_name}! You have successfully logged in.'
        )
        
        # Merge anonymous cart with user's existing cart
        if session_key:
            merged_items = merge_carts(user, session_key)
            if merged_items > 0:
                messages.info(
                    self.request, 
                    f'{merged_items} item(s) from your cart have been saved.'
                )
        
        return response
class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'
    
    def dispatch(self, request, *args, **kwargs):
        """Add farewell message before logout."""
        if request.user.is_authenticated:
            username = request.user.first_name or request.user.username
            messages.success(
                request, 
                f'Goodbye {username}! You have been successfully logged out.'
            )
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        """Add custom context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Logout'
        return context

class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Account created successfully for %(username)s! You can now log in.'
    
    def get_context_data(self, **kwargs):
        """Add custom context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Registration'
        return context
    
    def form_valid(self, form):
        """Handle successful registration with cart transfer."""
        # Save the user
        response = super().form_valid(form)
        
        # Transfer anonymous cart to the new user
        if self.request.session.session_key:
            merged_items = merge_carts(self.object, self.request.session.session_key)
            if merged_items > 0:
                messages.info(
                    self.request, 
                    f'{merged_items} item(s) have been added to your cart.'
                )
        
        return response

class ProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    
    def get_object(self):
        """Return the current user as the object to update."""
        return self.request.user
    
    def get_context_data(self, **kwargs):
        """Add orders data to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Profile'
        
        # Get user's orders with related items
        context['orders'] = Order.objects.filter(
            user=self.request.user
        ).prefetch_related(
            'orderitem_set__product'
        ).order_by('-created_at')
        
        return context
    
    def form_valid(self, form):
        """Handle successful profile update with custom messages."""
        # Check what changed before saving
        old_username = self.request.user.username
        new_username = form.cleaned_data.get('username')
        image_changed = 'image' in self.request.FILES
        
        # Save the form
        response = super().form_valid(form)
        
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
        
        messages.success(self.request, message)
        return response


class UsersCartView(LoginRequiredMixin, TemplateView):
    template_name = 'users/users_cart.html'