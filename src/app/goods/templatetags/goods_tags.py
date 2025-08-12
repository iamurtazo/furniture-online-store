from urllib.parse import urlencode
from django import template
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
import re
from goods.models import Categories

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

@register.filter(name='truncate_html')
def truncate_html(value, length=100):
    """
    Truncates HTML content while preserving HTML tags and adding ellipsis if needed.
    """
    if not value:
        return value
    
    # Convert to string if not already
    value = str(value)
    
    # If the content is shorter than the limit, return as is
    if len(strip_tags(value)) <= length:
        return mark_safe(value)
    
    # Create a pattern to find HTML tags
    tag_pattern = re.compile(r'<[^>]+>')
    
    # Track position in plain text
    plain_text_pos = 0
    result_parts = []
    last_end = 0
    
    # Find all HTML tags and their positions
    for match in tag_pattern.finditer(value):
        # Add text before this tag
        text_before = value[last_end:match.start()]
        if plain_text_pos + len(text_before) > length:
            # We need to truncate within this text
            remaining_chars = length - plain_text_pos
            if remaining_chars > 0:
                result_parts.append(text_before[:remaining_chars])
            result_parts.append('...')
            break
        else:
            result_parts.append(text_before)
            plain_text_pos += len(text_before)
        
        # Add the HTML tag (doesn't count towards length)
        result_parts.append(match.group())
        last_end = match.end()
    else:
        # Add remaining text if we didn't break out of loop
        remaining_text = value[last_end:]
        if plain_text_pos + len(remaining_text) > length:
            remaining_chars = length - plain_text_pos
            if remaining_chars > 0:
                result_parts.append(remaining_text[:remaining_chars])
            result_parts.append('...')
        else:
            result_parts.append(remaining_text)
    
    return mark_safe(''.join(result_parts))

@register.filter(name='mul')
def multiply(value, arg):
    """
    Multiplies the value by the argument.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter(name='add_tax')
def add_tax(value, tax_rate=0.08):
    """
    Adds tax to the value.
    """
    try:
        return float(value) * (1 + float(tax_rate))
    except (ValueError, TypeError):
        return 0