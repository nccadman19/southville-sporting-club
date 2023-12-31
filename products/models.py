from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100, unique=True)
    friendly_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default='N/A')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sizes = models.CharField(max_length=50, blank=True)
    size_quantity = models.JSONField(default=dict)
    image = models.ImageField(
        upload_to='product_images/',
        blank=True,
        null=True
    )
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_sizes_list(self):
        return [size.strip() for size in self.sizes.split(',') if size.strip()]

    def __str__(self):
        return self.name
