from django.db import models

from profiles.models import UserProfile
from products.models import Product


class WishList(models.Model):
    """
    Model to show all product items within the users wishlist
    """
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'WishList ({self.user_profile})'


class WishListItem(models.Model):
    """
    A model, allowing users to add
    individual products to their wishlist.
    """

    product = models.ForeignKey(Product, null=False,
                                blank=False, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(WishList, null=False,
                                 blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
