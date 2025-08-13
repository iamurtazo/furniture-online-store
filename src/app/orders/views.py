from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from django.db import transaction
from django.core.exceptions import ValidationError
from decimal import Decimal
from .forms import CreateOrderForm
from carts.models import Cart
from orders.models import Order, OrderItem

class CreateOrderView(LoginRequiredMixin, FormView):
    form_class = CreateOrderForm
    template_name = 'orders/create_order.html'
    success_url = reverse_lazy('users:profile')
    
    def get_context_data(self, **kwargs):
        """Add custom context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Order'
        return context
    
    def get_initial(self):
        """Pre-populate form with user data."""
        initial = super().get_initial()
        initial.update({
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'phone_number': getattr(self.request.user, 'phone_number', ''),
        })
        return initial
    
    def form_valid(self, form):
        """Process the order creation with stock management."""
        try:
            with transaction.atomic():
                user = self.request.user
                cart_items = Cart.objects.filter(user=user).select_related('product')
                
                # Check if cart is empty
                if not cart_items.exists():
                    messages.error(
                        self.request, 
                        "Your cart is empty. Please add items to your cart before placing an order."
                    )
                    return redirect('goods:index', 'all-categories')
                
                # Validate stock availability for all items first
                stock_errors = []
                for cart_item in cart_items:
                    if cart_item.product.quantity < cart_item.quantity:
                        stock_errors.append(
                            f"Only {cart_item.product.quantity} {cart_item.product.name} left in stock "
                            f"(you requested {cart_item.quantity})"
                        )
                
                if stock_errors:
                    for error in stock_errors:
                        messages.error(self.request, error)
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
                
                messages.success(
                    self.request, 
                    f"Order #{order.id:05d} created successfully! Total amount: ${total_amount:.2f}"
                )
                return super().form_valid(form)
                
        except ValidationError as e:
            messages.error(self.request, str(e))
            return redirect('users:users_cart')
        except Exception as e:
            messages.error(
                self.request, 
                "An error occurred while processing your order. Please try again."
            )
            return redirect('users:users_cart')

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'order_id'
    
    def get_queryset(self):
        """Restrict to orders belonging to the current user."""
        return Order.objects.filter(user=self.request.user).prefetch_related(
            'orderitem_set__product'
        )
    
    def get_context_data(self, **kwargs):
        """Add custom context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Order #{self.object.display_id()}'
        return context