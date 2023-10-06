from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    extra = 1 

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'full_name', 'email', 'phone_number', 'postcode', 'town_or_city', 'street_address1', 'street_address2')
    list_filter = ('postcode',)
    search_fields = ('order_number', 'full_name', 'email')
    inlines = [OrderLineItemInline]

admin.site.register(Order, OrderAdmin)
