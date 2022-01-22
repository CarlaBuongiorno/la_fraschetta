from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Category(models.Model):
    """
    Store categories details
    """
    class Meta:
        """Set verbose name"""
        verbose_name_plural = 'Categories'

    backend_name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.backend_name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Store Product details
    """
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=4,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    # Positive Integer -> https://docs.djangoproject.com/en/4.0/ref/models/fields/
    stock = models.PositiveSmallIntegerField(default=1,
                                             validators=[
                                                MaxValueValidator(500),
                                                MinValueValidator(0)
                                             ])

    def __str__(self):
        return self.name
