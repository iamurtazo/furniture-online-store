from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from carts.models import Cart
from goods.models import Products
from carts.utils import get_user_cart

# Create your views here.

class CartAddView(View):
    def post(self, request):
        """Handle adding product to cart via AJAX POST request."""
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
            # Handle authenticated user cart
            cart, created = Cart.objects.get_or_create(
                user=request.user, 
                product=product,
                defaults={'quantity': 1}
            )
            if not created:
                cart.quantity += 1
                cart.save()
        else:
            # Handle anonymous user cart
            if not request.session.session_key:
                request.session.create()
            
            cart, created = Cart.objects.get_or_create(
                session_key=request.session.session_key,
                product=product,
                defaults={'quantity': 1}
            )
            if not created:
                cart.quantity += 1
                cart.save()
        
        # Generate response data
        user_cart = get_user_cart(request)
        
        cart_items_html = render_to_string(
            'carts/includes/included_cart.html',
            {'carts': user_cart},
            request=request,
        )
        
        cart_button_html = render_to_string(
            'includes/cart_button.html',
            {'carts': user_cart},
            request=request,
        )
        
        return JsonResponse({
            "message": "Product added to cart successfully!",
            "cart_items_html": cart_items_html,
            "cart_button_html": cart_button_html,
            "cart_total_quantity": user_cart.total_quantity() if user_cart else 0,
            "has_items": user_cart.exists() if user_cart else False,
        })
    
    def get(self, request):
        """Return error for GET requests - this is AJAX POST only."""
        return JsonResponse({
            'error': 'Only POST method allowed'
        }, status=405)


class CartChangeView(View):
    def post(self, request):
        """Handle cart quantity changes via AJAX POST request."""
        cart_id = request.POST.get('cart_id')
        quantity = request.POST.get('quantity')
        
        # Validate input parameters
        if not cart_id or not quantity:
            return JsonResponse({
                'error': 'Cart ID and quantity are required'
            }, status=400)
        
        # Validate quantity value
        try:
            quantity = int(quantity)
            if quantity < 1:
                return JsonResponse({
                    'error': 'Quantity must be at least 1'
                }, status=400)
        except ValueError:
            return JsonResponse({
                'error': 'Invalid quantity value'
            }, status=400)
        
        # Update cart item
        try:
            cart = Cart.objects.get(id=cart_id)
            
            # Security check: ensure cart belongs to current user
            if request.user.is_authenticated and cart.user != request.user:
                return JsonResponse({
                    'error': 'Unauthorized access to cart item'
                }, status=403)
            
            cart.quantity = quantity
            cart.save()
            
            # Determine appropriate template based on referrer
            referer = request.META.get('HTTP_REFERER', '')
            if '/user/profile/' in referer:
                template_name = 'carts/includes/profile_cart_items.html'
            elif '/users-cart/' in referer:
                template_name = 'carts/includes/users_cart_items.html'
            else:
                template_name = 'carts/includes/included_cart.html'
            
            # Generate response HTML
            user_cart = get_user_cart(request)
            
            cart_items_html = render_to_string(
                template_name,
                {'carts': user_cart},
                request=request,
            )
            
            cart_button_html = render_to_string(
                'includes/cart_button.html',
                {'carts': user_cart},
                request=request,
            )
            
            return JsonResponse({
                "message": f"Cart updated to {quantity} items successfully!",
                "cart_items_html": cart_items_html,
                "cart_button_html": cart_button_html,
                "cart_total_quantity": user_cart.total_quantity() if user_cart.exists() else 0,
            })
            
        except Cart.DoesNotExist:
            return JsonResponse({
                'error': 'Cart item not found'
            }, status=404)
    
    def get(self, request):
        """Return error for GET requests - this is AJAX POST only."""
        return JsonResponse({
            'error': 'Only POST method allowed'
        }, status=405)

class CartRemoveView(View):
    def post(self, request):
        """Handle cart item removal via AJAX POST request."""
        cart_id = request.POST.get('cart_id')
        
        if not cart_id:
            return JsonResponse({
                'error': 'Cart ID is required'
            }, status=400)
        
        try:
            cart = Cart.objects.get(id=cart_id)
            
            # Security check: ensure cart belongs to current user
            if request.user.is_authenticated and cart.user != request.user:
                return JsonResponse({
                    'error': 'Unauthorized access to cart item'
                }, status=403)
            
            quantity = cart.quantity
            cart.delete()
            
            # Determine appropriate template based on referrer
            referer = request.META.get('HTTP_REFERER', '')
            if '/user/profile/' in referer:
                template_name = 'carts/includes/profile_cart_items.html'
            elif '/users-cart/' in referer:
                template_name = 'carts/includes/users_cart_items.html'
            else:
                template_name = 'carts/includes/included_cart.html'
            
            # Generate response HTML
            user_cart = get_user_cart(request)
            
            cart_items_html = render_to_string(
                template_name,
                {'carts': user_cart},
                request=request,
            )
            
            cart_button_html = render_to_string(
                'includes/cart_button.html',
                {'carts': user_cart},
                request=request,
            )
            
            return JsonResponse({
                "message": "Product removed from cart successfully!",
                "cart_items_html": cart_items_html,
                "cart_button_html": cart_button_html,
                "quantity_deleted": quantity,
                "cart_total_quantity": user_cart.total_quantity() if user_cart.exists() else 0,
                "has_items": user_cart.exists() if user_cart else False,
            })
            
        except Cart.DoesNotExist:
            return JsonResponse({
                'error': 'Cart item not found'
            }, status=404)
    
    def get(self, request):
        """Return error for GET requests - this is AJAX POST only."""
        return JsonResponse({
            'error': 'Only POST method allowed'
        }, status=405)
    
    



