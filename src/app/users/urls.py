from django.urls import path
from users.views import (
    CustomLoginView, 
    CustomLogoutView, 
    RegistrationView, 
    ProfileView, 
    UsersCartView
)

app_name = 'users'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users-cart/', UsersCartView.as_view(), name='users_cart')
]
