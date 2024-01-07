from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'color',
        'price',
        'display_categories',
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

    def display_categories(self, obj):
        return ', '.join([category.name for category in obj.category.all()])
    display_categories.short_description = 'Category'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'updated_at')
    search_fields = ('name', 'friendly_name')
    prepopulated_fields = {'friendly_name': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
