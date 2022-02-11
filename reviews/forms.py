from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form to add/edit a review
    """
    class Meta:
        """Set up form for review model """
        model = Review
        fields = ['rating', 'review']

    review = forms.CharField(
        widget=forms.Textarea(attrs={
                            'rows': '4',
                            'placeholder': 'Add a review'})
    )
