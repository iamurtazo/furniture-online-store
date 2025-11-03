from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import DetailView, ListView
from django.http import Http404
from .models import *
from .utils import q_search, prepare_search_results

# Create your views here.
class CatalogView(ListView):
    model = Products
    template_name = 'goods/catalog.html'
    context_object_name = 'goods'
    paginate_by = 4
    
    def get_queryset(self):
        # Get URL parameters
        category_slug = self.kwargs.get('category_slug')
        query = self.request.GET.get('q')
        on_sale = self.request.GET.get('on_sale')
        order_by = self.request.GET.get('order_by')
        
        # Base queryset logic
        if category_slug == 'all-categories':
            # Show all products
            queryset = Products.objects.all()
        elif query:
            # Use search functionality
            queryset = q_search(query)
        else:
            # Filter by category slug
            try:
                queryset = Products.objects.filter(category__slug=category_slug)
                if not queryset.exists():
                    raise Http404("Category not found")
            except Products.DoesNotExist:
                raise Http404("Category not found")
        
        # Apply filters
        if on_sale:
            queryset = queryset.filter(discount__gt=0)
        
        # Apply ordering
        if order_by and order_by != 'default':
            if order_by == '-price':
                queryset = queryset.order_by('-price')
            else:
                queryset = queryset.order_by(order_by)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get URL parameters
        category_slug = self.kwargs.get('category_slug')
        query = self.request.GET.get('q', '')
        on_sale = self.request.GET.get('on_sale')
        order_by = self.request.GET.get('order_by')
        
        # Determine if this is a search
        is_search = bool(query)
        
        # Apply search highlighting if needed - DON'T modify page_obj directly
        if is_search and context['goods']:
            # Create a new list with highlighted products for template use
            page_obj = context['page_obj']
            highlighted_products = prepare_search_results(page_obj.object_list, query)
            # Add as separate context variable instead of modifying page_obj
            context['highlighted_goods'] = highlighted_products
        
        # Add custom context
        context.update({
            'title': 'Search Results' if is_search else 'Catalog - Home',
            'slug_url': category_slug,
            'on_sale': on_sale,
            'order_by': order_by,
            'current_filters': self.request.GET.urlencode(),
            'is_search': is_search,
            'search_query': query,
            # Fix this line - use page_obj instead of goods for pagination
            'has_results': len(context['page_obj'].object_list) > 0 if context.get('page_obj') else len(context.get('object_list', [])) > 0,
        })
        
        return context


class ProductDetailView(DetailView):
    model = Products
    template_name = 'goods/product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Product - Home',
        })
        return context