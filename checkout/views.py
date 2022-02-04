from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    View to display checkout page
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K3djBIxKeITzM6mvn1ZJbg45EqEwk3jFE8k5o09TL816IyG0cLjlhv9D73JDN5DO0DU6fdvm7nFT8muSkKWs26l00IB20tpRm',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
