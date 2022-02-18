from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from wishlist.models import WishList


@login_required
def wishlist(request):
    """
    A view to render the user's wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = WishList.objects.filter(user_profile=user)

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """
    View to add products to wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    item = WishList.objects.create(
        user_profile=user,
        product=product
    )
    messages.success(request, f'{product.name} has been added to your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def remove_from_wishlist(request, product_id):
    """
    View to remove products from wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    # get the product to be removed from WishList
    product = get_object_or_404(Product, pk=product_id)
    # find a match to the product and user, then .delete() it
    WishList.objects.filter(product=product, user_profile=user).delete()

    messages.info(request, f'{product.name} has been removed from your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))
