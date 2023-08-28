from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower

def product_list(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

            if not products:
                messages.error(request, "No products match your search criteria.")
                return redirect(reverse('nothing_found'))

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'title': 'Product List',
        'search_term': query,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    # Retrieve the product with the specified ID or return a 404 error if not found
    product = get_object_or_404(Product, pk=product_id)
    
    context = {'product': product, 'title': 'Product Detail'}
    return render(request, 'products/product_detail.html', context)

def nothing_found(request):
    return render(request, 'products/nothing_found.html')
