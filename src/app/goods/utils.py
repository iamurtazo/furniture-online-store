from django.db.models import Q
from django.utils.html import format_html
import re
from .models import Products

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 2]
    
    q_objects = Q()
    
    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)
        
    return Products.objects.filter(q_objects)

def highlight_search_terms(text, query):
    """
    Highlights search terms in text with HTML highlighting.
    Returns the text with search terms wrapped in <mark> tags.
    """
    if not text or not query:
        return text
    
    # Get keywords (filter out short words like in q_search)
    keywords = [word for word in query.split() if len(word) > 2]
    
    if not keywords:
        return text
    
    # Create a pattern that matches any of the keywords (case-insensitive)
    pattern = '|'.join(re.escape(keyword) for keyword in keywords)
    
    # Highlight the matches with <mark> tags
    highlighted_text = re.sub(
        f'({pattern})', 
        r'<mark class="search-highlight">\1</mark>', 
        text, 
        flags=re.IGNORECASE
    )
    
    return format_html(highlighted_text)

def prepare_search_results(products, query):
    """
    Prepares products for display by adding highlighted versions of name and description.
    """
    enhanced_products = []
    
    for product in products:
        # Create a copy of the product with highlighted fields
        product.highlighted_name = highlight_search_terms(product.name, query)
        product.highlighted_description = highlight_search_terms(product.description, query)
        enhanced_products.append(product)
    
    return enhanced_products
    