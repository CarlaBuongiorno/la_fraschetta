from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings


# Credit -> https://docs.djangoproject.com/en/4.0/topics/forms/
def contact(request):
    """View to render contact page"""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = [settings.EMAIL_HOST_USER,]

            send_mail(f'You have received a message from {name}: {email}',
                      subject, message, [recipients])
            messages.success(
                request, 'Your message has been sent!')
            # redirect to contact page
            return redirect(reverse('contact'))
        else:
            messages.error(
                request, 'There was a problem sending your message. \
                    Please try again.')
    else:
        # Create a blank form
        form = ContactForm()

        template = 'contact/contact.html'
        context = {
            'form': form,
        }

    return render(request, template, context)
