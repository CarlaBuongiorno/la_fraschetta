from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Admin setting to display a list of products
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'stock',
        'rating',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin setting to display a list of categories
    """
    list_display = (
        'friendly_name',
        'backend_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
