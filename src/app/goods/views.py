from django.shortcuts import render
from .models import *

# Create your views here.
def catalog(request):
    
    goods = Products.objects.all()
    
    context = {
        'title': 'Catalog - Home',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_id):
    
    product = Products.objects.get(id=product_id)
    
    context = {
        'title': 'Product - Home',
        'product': product,
    }
    return render(request, 'goods/product.html', context)

# def product(request, product_slug):
    
#     product = Products.objects.get(slug=product_slug)
    
#     context = {
#         'title': 'Product - Home',
#         'product': product,
#     }
#     return render(request, 'goods/product.html', context)