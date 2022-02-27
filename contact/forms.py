from django import forms


class ContactForm(forms.Form):
    """
    Form to collect contact form details
    """
    name = forms.CharField(min_length=2,
                           max_length=100,
                           label='Name')
    email = forms.EmailField(widget=forms.EmailInput(),
                             label='Your Email Address')
    subject = forms.CharField(min_length=3,
                              max_length=40,
                              label='Subject')
    message = forms.CharField(min_length=5,
                              max_length=300,
                              widget=forms.Textarea(),
                              label='Message')

    def __init__(self, *args, **kwargs):
        """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'message': 'Your Message',
            'subject': 'Subject',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-green green \
                contact-form-input'
            self.fields[field].label = False
