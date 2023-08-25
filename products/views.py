from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

def product_list(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

            if not products:
                messages.error(request, "No products match your search criteria.")
                return redirect(reverse('products'))

    context = {
        'products': products,
        'title': 'Product List',
        'search_term': query,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    # Retrieve the product with the specified ID or return a 404 error if not found
    product = get_object_or_404(Product, pk=product_id)
    
    context = {'product': product, 'title': 'Product Detail'}
    return render(request, 'products/product_detail.html', context)