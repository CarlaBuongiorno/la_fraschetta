from django.contrib import admin
from .models import Review


admin.site.register(Review)


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin settings to display list of Reviews
    Ordered by date created and ratings
    filter by ratings
    """

    model = Review
    list_display = (
        'product',
        'created_on',
        'rating',
        'user_profile',
        'review',
    )

    ordering = ('-created_on', '-rating', )
    list_filter = ('rating',)
