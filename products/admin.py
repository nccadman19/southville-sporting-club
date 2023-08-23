from django.contrib import admin
from .models import Product, Category

# Models

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'category',
        'updated_at'
    )
    list_filter = (
        'category',
        'updated_at'
    )
    search_fields = ('sku', 'name')
    list_editable = ('price',)
    list_per_page = 20
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'updated_at')
    search_fields = ('name', 'friendly_name')
    prepopulated_fields = {'friendly_name': ('name',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)