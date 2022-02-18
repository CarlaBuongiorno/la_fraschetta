from django.db import models

from profiles.models import UserProfile
from products.models import Product


class WishList(models.Model):
    """
    Model to show all product items within the users wishlist
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'WishList ({self.user_profile})'
