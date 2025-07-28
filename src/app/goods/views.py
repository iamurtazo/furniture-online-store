from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *

# Create your views here.
def catalog(request, category_slug):
    
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None) 
    order_by = request.GET.get('order_by', None)  
    
    # Base queryset
    if category_slug == 'all-categories':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
    
    if on_sale:
        goods = goods.filter(discount__gt=0)
    
    
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)
    # elif order_by == '-price':
    #    goods = goods.order_by('-price')
    
    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
    
    context = {
        'title': 'Catalog - Home',
        'goods': current_page,
        'slug_url': category_slug,
        'on_sale': on_sale,
        'order_by': order_by,
        'current_filters': request.GET.urlencode(),  # Pass all current GET parameters
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