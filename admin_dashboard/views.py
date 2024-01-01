import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from checkout.models import Order
from products.models import Product
from django.db.models import Sum

# Import timedelta from datetime
from datetime import timedelta

@login_required
def admin_dashboard(request):
    if request.user.is_staff:
        # Get the current date and time in the project's timezone
        today = timezone.now()

        # Calculate the first day of the current month (naive datetime)
        first_day_of_month_naive = today.replace(day=1)

        # Calculate the first moment of the first day of the current month (midnight)
        first_moment_of_month_naive = datetime.datetime(first_day_of_month_naive.year, first_day_of_month_naive.month, first_day_of_month_naive.day)

        # Calculate the last day of the current month (naive datetime)
        last_day_of_month_naive = (first_day_of_month_naive + timedelta(days=32)).replace(day=1) - timedelta(days=1)

        # Calculate the last moment of the last day of the current month (23:59:59)
        last_moment_of_month_naive = datetime.datetime(last_day_of_month_naive.year, last_day_of_month_naive.month, last_day_of_month_naive.day, 23, 59, 59, 999999)

        # Convert first and last day of the month to UTC (make them aware)
        first_moment_of_month_utc = timezone.make_aware(first_moment_of_month_naive, timezone.utc)
        last_moment_of_month_utc = timezone.make_aware(last_moment_of_month_naive, timezone.utc)

        # Calculate sales for the current month
        monthly_sales = Order.objects.filter(date__gte=first_moment_of_month_utc, date__lte=last_moment_of_month_utc).aggregate(total_sales=Sum('order_total'))['total_sales'] or 0

        return render(request, 'admin_dashboard/admin_dashboard.html', {'monthly_sales_figure': monthly_sales})
    else:
        # User is not an admin, return a 404 Not Found response
        return HttpResponseNotFound()



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