from carts.models import Cart

def merge_carts(user, session_key):
    """
    Merge anonymous cart items with existing user cart items.
    
    When a user logs in or registers, this function merges their
    anonymous cart (identified by session_key) with any existing
    cart items they may have from previous sessions.
    
    Args:
        user: The authenticated user
        session_key: The session key for anonymous cart items
    
    Returns:
        int: Number of items merged
    """
    if not session_key:
        return 0
    
    # Get anonymous cart items
    anonymous_carts = Cart.objects.filter(session_key=session_key)
    
    if not anonymous_carts.exists():
        return 0
    
    merged_count = 0
    
    for anon_cart in anonymous_carts:
        # Check if user already has this product in their cart
        existing_cart = Cart.objects.filter(
            user=user,
            product=anon_cart.product
        ).first()
        
        if existing_cart:
            # Merge quantities
            existing_cart.quantity += anon_cart.quantity
            existing_cart.save()
            # Delete the anonymous cart item
            anon_cart.delete()
        else:
            # Transfer the cart item to the user
            anon_cart.user = user
            anon_cart.session_key = None
            anon_cart.save()
        
        merged_count += 1
    
    return merged_count