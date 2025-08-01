from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *
from .utils import q_search, prepare_search_results

# Create your views here.
def catalog(request, category_slug=None):
    
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None) 
    order_by = request.GET.get('order_by', None)  
    query = request.GET.get('q', None)
    
    # Initialize search context
    is_search = bool(query)
    search_query = query if query else ''
    
    # Base queryset
    if category_slug == 'all-categories':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
    if on_sale:
        goods = goods.filter(discount__gt=0)
    
    
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)
    elif order_by == '-price':
       goods = goods.order_by('-price')
    
    # Check if we have results before pagination
    has_results = goods.exists() if hasattr(goods, 'exists') else len(goods) > 0
    
    # Apply pagination only if we have results
    if has_results:
        paginator = Paginator(goods, 3)
        current_page = paginator.page(int(page))
        
        # Apply highlighting for search results
        if is_search:
            highlighted_products = prepare_search_results(current_page.object_list, query)
            current_page.object_list = highlighted_products
    else:
        # Create empty paginator result for no results
        paginator = Paginator([], 3)
        current_page = paginator.page(1)
    
    context = {
        'title': 'Search Results' if is_search else 'Catalog - Home',
        'goods': current_page,
        'slug_url': category_slug,
        'on_sale': on_sale,
        'order_by': order_by,
        'current_filters': request.GET.urlencode(),  # Pass all current GET parameters
        'is_search': is_search,
        'search_query': search_query,
        'has_results': has_results,
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