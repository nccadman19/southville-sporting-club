from products.models import Product
from .models import Order, OrderLineItem

def update_total_quantity(order):
    # Retrieve the order line items associated with the order
    order_line_items = order.lineitems.all()

    for item in order_line_items:
        product = item.product
        quantity = item.quantity

        # Update the product's size_quantity dictionary
        if item.product_size in product.size_quantity:
            product.size_quantity[item.product_size] -= quantity
            product.save()

