from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from wishlist.models import WishListItem


@login_required
def wishlist(request):
    """
    A view to render the user's wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    user_wishlist = user.wishlist_items.all()

    if user_wishlist:
        items = WishListItem.objects.filter(
            user_wishlist__in=user_wishlist)

    else:
        items = []

    template = 'wishlist/wishlist.html'
    context = {
        'items': items,
    }
    return render(request, template, context)
