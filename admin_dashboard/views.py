from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from checkout.models import Order
from products.models import Product

@login_required
def order_list(request):
    if request.user.is_staff:
        orders = Order.objects.all().prefetch_related('lineitems')
        return render(request, 'admin_dashboard/order_list.html', {'orders': orders})
    else:
        # User is not an admin, return a 404 Not Found response
        return HttpResponseNotFound()

@login_required
def stock_list(request):
    products = Product.objects.all()
    return render(request, 'admin_dashboard/stock_list.html', {'products': products})