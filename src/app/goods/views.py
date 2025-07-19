from django.shortcuts import render


# Create your views here.
def catalog(request):
    context = {
        'title': 'Catalog - Home',
        'goods': [
            {
                'image': 'deps/images/goods/set of tea table and three chairs.jpg',
                'name': 'Tea table and three chairs',
                'description': 'Set of three chairs and designer table for the living room.',
                'price': 150.00
            },
            {
                'image': 'deps/images/goods/set of tea table and two chairs.jpg',
                'name': 'Tea table and two chairs',
                'description': 'Set of table and two chairs in minimalist style.',
                'price': 93.00
            },
            {
                'image': 'deps/images/goods/double bed.jpg',
                'name': 'Double bed',
                'description': 'Double bed with headboard and very orthopedic.',
                'price': 670.00
            },
            {
                'image': 'deps/images/goods/kitchen table.jpg',
                'name': 'Kitchen table with sink',
                'description': 'Kitchen table for dining with built-in sink and chairs.',
                'price': 365.00
            },
            {
                'image': 'deps/images/goods/kitchen table 2.jpg',
                'name': 'Kitchen table with built-ins',
                'description': 'Kitchen table with built-in stove and sink. Lots of shelves and generally beautiful.',
                'price': 430.00
            },
            {
                'image': 'deps/images/goods/corner sofa.jpg',
                'name': 'Corner sofa for living room',
                'description': 'Corner sofa, unfolds into a double bed, perfect for the living room and receiving guests!',
                'price': 610.00
            },
            {
                'image': 'deps/images/goods/bedside table.jpg',
                'name': 'Bedside table',
                'description': 'Bedside table with two drawers (flower not included).',
                'price': 55.00
            },
            {
                'image': 'deps/images/goods/sofa.jpg',
                'name': 'Ordinary sofa',
                'description': 'Sofa, also known as ordinary sofa, nothing remarkable to describe.',
                'price': 190.00
            },
            {
                'image': 'deps/images/goods/office chair.jpg',
                'name': 'Office chair',
                'description': 'Product description about how cool it is, but it\'s a chair, what can you say...',
                'price': 30.00
            },
            {
                'image': 'deps/images/goods/plants.jpg',
                'name': 'Plant',
                'description': 'Plant to decorate your interior will bring freshness and serenity to the atmosphere.',
                'price': 10.00
            },
            {
                'image': 'deps/images/goods/flower.jpg',
                'name': 'Stylized flower',
                'description': 'Designer flower (possibly artificial) for interior decoration.',
                'price': 15.00
            },
            {
                'image': 'deps/images/goods/strange table.jpg',
                'name': 'Bedside table',
                'description': 'Table, quite strange looking, but suitable for placement next to the bed.',
                'price': 25.00
            },
        ],
    }
    return render(request, 'goods/catalog.html', context=context)


def product(request):
    return render(request, 'goods/product.html')