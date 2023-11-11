from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.urls import reverse

from .models import Product, Category
from .forms import ProductForm

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
    products = Product.objects.annotate(available_sizes_count=Count('size_quantity', filter=~Q(size_quantity__exact={})))\
                               .filter(available_sizes_count__gt=0)
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

    if products.exists():
        context = {
            'products': products,
            'title': 'Product List',
            'search_term': query,
            'current_sorting': current_sorting,
            'categories': categories,
            'selected_category': category,
        }
        return render(request, 'products/products.html', context)
    else:
        # Redirect to the "nothing found" view when no results are found
        return redirect('nothing_found')

def product_detail(request, product_id):
    # Retrieve the product with the specified ID or return a 404 error if not found
    product = get_object_or_404(Product, pk=product_id)

    # Check if the product has available sizes
    has_available_sizes = product.has_available_sizes()

    context = {'product': product, 'has_available_sizes': has_available_sizes, 'title': 'Product Detail'}
    return render(request, 'products/product_detail.html', context)

def nothing_found(request):
    return render(request, 'products/nothing_found.html')

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Retrieve the selected sizes
            selected_sizes = request.POST.getlist('size')
            sizes_csv = ', '.join(selected_sizes)

            # Create and save the product instance with the sizes
            product = form.save(commit=False)
            product.sizes = sizes_csv
            product.save()

            # Save selected categories
            selected_categories = request.POST.getlist('category')
            product.category.clear()  # Clear existing categories
            for category_id in selected_categories:
                category = Category.objects.get(pk=category_id)
                product.category.add(category)
            product.save()

            messages.success(request, 'Successfully added product!')

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add the product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    # Retrieve the product information  
    product = get_object_or_404(Product, pk=product_id)
    
    # Retrieve the selected category IDs for the product
    selected_category_ids = product.category.all().values_list('id', flat=True)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            selected_sizes = request.POST.getlist('size')
            product.sizes = ', '.join(selected_sizes)
            form.save()
            messages.success(request, 'Successfully updated product!')

            # Print the full form data
            print("Full Form Data:", request.POST)

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'size_quantity': product.size_quantity,
        'selected_category_ids': selected_category_ids,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
