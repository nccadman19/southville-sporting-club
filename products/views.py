from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    context = {'products': products, 'title': 'Product List'}
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    # Retrieve the product with the specified ID or return a 404 error if not found
    product = get_object_or_404(Product, pk=product_id)
    
    context = {'product': product, 'title': 'Product Detail'}
    return render(request, 'products/product_detail.html', context)