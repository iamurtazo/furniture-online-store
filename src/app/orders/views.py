from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateOrderForm
from carts.models import Cart
from orders.models import Order, OrderItem
from django.db import transaction
from django.core.exceptions import ValidationError
from decimal import Decimal

@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user).select_related('product')
                    
                    # Check if cart is empty
                    if not cart_items.exists():
                        messages.error(request, "Your cart is empty. Please add items to your cart before placing an order.")
                        return redirect('goods:index', 'all-categories')
                    
                    # Validate stock availability for all items first
                    stock_errors = []
                    for cart_item in cart_items:
                        if cart_item.product.quantity < cart_item.quantity:
                            stock_errors.append(f"Only {cart_item.product.quantity} {cart_item.product.name} left in stock (you requested {cart_item.quantity})")
                    
                    if stock_errors:
                        for error in stock_errors:
                            messages.error(request, error)
                        return redirect('users:users_cart')
                    
                    # Set delivery requirements
                    requires_delivery = form.cleaned_data.get('requires_delivery', False)
                    delivery_address = form.cleaned_data.get('delivery_address', '') if requires_delivery else ''
                    
                    # Create order
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                        requires_delivery=requires_delivery,
                        delivery_address=delivery_address,
                        payment_on_get=form.cleaned_data.get('payment_on_get', False),
                    )
                    
                    # Create order items and update stock
                    total_amount = Decimal('0.00')
                    for cart_item in cart_items:
                        product = cart_item.product
                        item_price = product.get_discounted_price()
                        item_total = item_price * cart_item.quantity
                        total_amount += item_total
                        
                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=product.name,
                            quantity=cart_item.quantity,
                            price=item_price,
                        )
                        
                        # Update product stock
                        product.quantity -= cart_item.quantity
                        product.save(update_fields=['quantity'])
                    
                    # Clear cart
                    cart_items.delete()
                    
                    messages.success(request, f"Order #{order.id:05d} created successfully! Total amount: ${total_amount:.2f}")
                    return redirect('users:profile')                
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('users:users_cart')
            except Exception as e:
                messages.error(request, "An error occurred while processing your order. Please try again.")
                return redirect('users:users_cart')                 
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'phone_number': getattr(request.user, 'phone_number', ''),
        }
        
        form = CreateOrderForm(initial=initial)
    
    context = {
        'title': 'Create Order',
        'form': form,
    }
    
    return render(request, 'orders/create_order.html', context)

def order_detail(request):
    pass