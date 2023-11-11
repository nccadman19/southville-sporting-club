from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        if '_' in item_id:
            product_id, selected_size = item_id.split('_')
            product = get_object_or_404(Product, pk=product_id)
            item_total = quantity * product.price
            total += item_total
            product_count += quantity

            # Check if the product has an image, and handle it accordingly
            if product.image:
                image_url = product.image.url
            else:
                image_url = f"{settings.MEDIA_URL}no-image.webp"

            bag_items.append({
                'item_id': product.id,
                'quantity': quantity,
                'product': product,
                'size': selected_size,
                'item_total': item_total,
                'image_url': image_url,
            })

    # Access the thresholds from settings
    thresholds = settings.DELIVERY_THRESHOLDS

    delivery_cost = Decimal('04.99')
    first_class_delivery_cost = Decimal('09.99')

    # Check if the order total is over £100 for free standard delivery
    if total >= Decimal('100.00'):
        delivery_cost = Decimal('00.00')

    # Check if the order total is over £150 for free 1st class delivery
    if total >= Decimal('150.00'):
        first_class_delivery_cost = Decimal('00.00')

    grand_total = total + delivery_cost
    first_class_total = total + first_class_delivery_cost

    uk_mainland_standard_delta = thresholds['UK_MAINLAND_STANDARD'] - total
    uk_mainland_1st_class_delta = thresholds['UK_MAINLAND_1ST_CLASS'] - total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'thresholds': thresholds,
        'delivery_cost': delivery_cost,
        'first_class_delivery_cost': first_class_delivery_cost,
        'grand_total': grand_total,
        'first_class_total': first_class_total,
        'uk_mainland_standard_delta': uk_mainland_standard_delta,
        'uk_mainland_1st_class_delta': uk_mainland_1st_class_delta,
    }

    return context
