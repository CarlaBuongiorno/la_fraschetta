from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Set up form to collect order details during checkout
    """
    class Meta:
        """
        Define form meta properties
        """
        model = Order
        fields = ('full_name', 'email', 'delivery_street_address1',
                  'delivery_street_address2', 'delivery_town_or_city',
                  'delivery_postcode', 'delivery_country',)

    def __init__(self, *args, **kwargs):
        """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'delivery_postcode': 'Postal Code',
            'delivery_town_or_city': 'Town or City',
            'delivery_street_address1': 'Street Address 1',
            'delivery_street_address2': 'Street Address 2',
            'delivery_country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
