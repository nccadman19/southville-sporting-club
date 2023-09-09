from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

def bag_contents(request):
    # Create a dictionary of the shopping bag's contents.
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        item_total = quantity * product.price
        total += item_total
        product_count += quantity
        bag_items.append({
            'item_id': item.id,
            'quantity': quantity,
            'product': product,
            'item_total': item_total,
        })

    # Access the thresholds from settings
    thresholds = settings.DELIVERY_THRESHOLDS

    delivery_cost = Decimal('00.00')
    fast_delivery_cost = Decimal('00.00')
    europe_delivery_cost = Decimal('00.00')
    rest_worldwide_delivery_cost = Decimal('00.00')

    if total < thresholds['UK_MAINLAND_STANDARD']:
        delivery_cost = Decimal('03.00')
    if total < thresholds['UK_MAINLAND_1ST_CLASS']:
        fast_delivery_cost = Decimal('05.00')
    if total < thresholds['EUROPE_MAINLAND']:
        delivery_cost = Decimal('10.00')
    if total < thresholds['REST_WORLDWIDE']:
        fast_delivery_cost = Decimal('16.99')

    if total < thresholds['UK_MAINLAND_STANDARD']:
        delivery_cost = Decimal('00.00')
    if total < thresholds['UK_MAINLAND_1ST_CLASS']:
        fast_delivery_cost = Decimal('00.00')
    if total >= thresholds['EUROPE_MAINLAND']:
        delivery_cost = Decimal('00.00')
    if total >= thresholds['REST_WORLDWIDE']:
        fast_delivery_cost = Decimal('00.00')

    grand_total = total + delivery_cost  # Total with standard delivery cost
    fast_delivery_total = total + fast_delivery_cost  # Total with fast delivery cost

    # Calculate the deltas for thresholds
    uk_mainland_1st_class_delta = thresholds['UK_MAINLAND_1ST_CLASS'] - total
    uk_mainland_standard_delta = thresholds['UK_MAINLAND_STANDARD'] - total
    europe_mainland_delta = thresholds['EUROPE_MAINLAND'] - total
    rest_worldwide_delta = thresholds['REST_WORLDWIDE'] - total

    grand_total = delivery_cost + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'thresholds': thresholds,
        'delivery_cost': delivery_cost,
        'fast_delivery_cost': fast_delivery_cost,
        'europe_delivery_cost': europe_delivery_cost,
        'rest_worldwide_delivery_cost': rest_worldwide_delivery_cost,
        'grand_total': grand_total,
        'fast_delivery_total': fast_delivery_total,
        'uk_mainland_1st_class_delta': uk_mainland_1st_class_delta,
        'uk_mainland_standard_delta': uk_mainland_standard_delta,
        'europe_mainland_delta': europe_mainland_delta,
        'rest_worldwide_delta': rest_worldwide_delta,
    }

    return context
