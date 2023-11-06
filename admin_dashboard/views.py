from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product
from checkout.models import Order

@login_required
def order_list(request):
    if request.user.is_staff:
        # User is an admin, so allow access to the view
        return render(request, 'order_list.html')
    else:
        # User is not an admin, return a 404 Not Found response
        return HttpResponseNotFound()

@login_required
def stock_list(request):
    # Your view logic here
    return render(request, 'admin_dashboard/stock_list.html')