from django.shortcuts import render, redirect
from carts.models import Cart
from goods.models import Products
from django.template.loader import render_to_string
from django.http import JsonResponse
from carts.utils import get_user_cart

# Create your views here.

def cart_add(request):
    if request.method == 'POST':
        product_id = request.POST.get('good_id')
        
        if not product_id:
            return JsonResponse({
                'error': 'Product ID is required'
            }, status=400)
        
        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return JsonResponse({
                'error': 'Product not found'
            }, status=404)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)

            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(user=request.user, product=product, quantity=1)
                
            user_cart = get_user_cart(request)
            
            cart_items_html = render_to_string(
                'carts/includes/included_cart.html',
                {'carts': user_cart},
                request=request,
            )
            
            response_data = {
                "message": "Product added to cart successfully!",
                "cart_items_html": cart_items_html,
                "cart_total_quantity": user_cart.total_quantity() if user_cart else 0,
            }

            return JsonResponse(response_data)
        else:
            return JsonResponse({
                'error': 'Please login to add items to cart'
            }, status=401)
    
    return JsonResponse({
        'error': 'Invalid request method'
    }, status=405)


def cart_change(request, product_slug):
    pass

def cart_remove(request, cart_id):
    
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    
    # Check if request came from profile page and preserve cart tab
    referer = request.META.get('HTTP_REFERER', '')
    if '/user/profile/' in referer:
        return redirect('/user/profile/#cart')
    
    return redirect(request.META['HTTP_REFERER'])



