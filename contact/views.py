from django.shortcuts import render, redirect, reverse

from .forms import ContactForm


def contact(request):
    """View to render contact page"""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required

            # redirect to a new URL?:
            return redirect(reverse('contact'))

    else:
        # Create a blank form
        form = ContactForm()

        template = 'contact/contact.html'
        context = {
            'form': form,
        }

    return render(request, template, context)
