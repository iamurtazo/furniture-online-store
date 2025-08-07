from django.shortcuts import render
from goods.models import Categories

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'description': 'Furniture Store - Home',
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    context = {
        'title': 'About Us',
        'description': 'Welcome to our premium furniture store! We are dedicated to providing high-quality, stylish furniture that transforms your house into a home. With years of experience in the furniture industry, we carefully curate each piece to ensure it meets our standards of quality, comfort, and design.'
    }
    return render(request, 'main/about.html', context=context)

def delivery_payment(request):
    context = {
        'title': 'Delivery and Payment',
        'description': 'Learn about our delivery options and payment methods.'
    }
    return render(request, 'main/delivery_payment.html', context=context)

def contact_info(request):
    context = {
        'title': 'Contact Information',
        'description': 'Get in touch with us for any questions or support.'
    }
    return render(request, 'main/contact_info.html', context=context)