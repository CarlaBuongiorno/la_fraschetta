from django.db import models

from products.models import Product


class Order(models.Model):
    """
    Stores order details
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    delivery_street_address1 = models.CharField(max_length=80, null=False,
                                                blank=False)
    delivery_street_address2 = models.CharField(max_length=80, null=True,
                                                blank=True)
    delivery_postcode = models.CharField(max_length=20, null=False,
                                         blank=False)
    delivery_town_or_city = models.CharField(max_length=40, null=False,
                                             blank=False)
    delivery_country = models.CharField(max_length=40, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')
