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
        'description': 'Text about how great this online store is.'
    }
    return render(request, 'main/about.html', context=context)