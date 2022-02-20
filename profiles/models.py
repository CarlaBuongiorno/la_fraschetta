from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries import Countries
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining
    delivery information and order history
    """

    class G8Countries(Countries):
        """ Restrict delivery countries to NL only """
        only = ['NL']

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=35, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True,
                           max_length=80, blank=True,
                           countries=G8Countries)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
