from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower

synonyms = {
    "hoody": "hoodie",
    "joggers": "sweatpants",
    "jogger": "sweatpants",
    "tshirt": "t-shirt",

}

def preprocess_query(query):
    query = query.lower()
    # Check if the query is in the synonyms dictionary
    if query in synonyms:
        return synonyms[query]
    return query


def product_list(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    query = request.GET.get('q')
    sort = request.GET.get('sort', 'name') 
    category = request.GET.get('category', 'all')
    direction = request.GET.get('direction', 'asc')

    if sort == 'name':
        sortkey = 'lower_name'
        products = products.annotate(lower_name=Lower('name'))
    else:
        sortkey = sort

    if direction == 'desc':
        sortkey = f'-{sortkey}'

    if query:
        # Remove leading and trailing spaces from the query
        query = preprocess_query(query.strip().lower())
        queries = Q(name__icontains=query) | Q(description__icontains=query)

        # Check if the query contains a space and split it into words
        if ' ' in query:
            query_parts = query.split(' ')
            for part in query_parts:
                queries |= Q(color__icontains=part.strip())
        else:
            queries |= Q(color__icontains=query)

        products = products.filter(queries)

    if category != 'all':
        products = products.filter(category__name=category)

    products = products.order_by(sortkey)
    current_sorting = f'{sort}_{direction}'
    categories = Category.objects.all()

    context = {
        'products': products,
        'title': 'Product List',
        'search_term': query,
        'current_sorting': current_sorting,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    # Retrieve the product with the specified ID or return a 404 error if not found
    product = get_object_or_404(Product, pk=product_id)
    
    context = {'product': product, 'title': 'Product Detail'}
    return render(request, 'products/product_detail.html', context)

def nothing_found(request):
    return render(request, 'products/nothing_found.html')
