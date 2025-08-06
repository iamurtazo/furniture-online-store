from carts.models import Cart

def get_user_cart(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).order_by('created_at', 'id', 'product__name')
    else:
        return Cart.objects.none()
    