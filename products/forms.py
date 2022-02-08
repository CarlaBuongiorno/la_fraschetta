from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Set up model form to add a product
    """
    class Meta:
        """Set fields from product model"""
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Display category names as choice fields in the form
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-green'
