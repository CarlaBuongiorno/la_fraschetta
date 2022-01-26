from django.conf import settings
from .models import Category


def all_categories(request):

    category_list = Category.objects.all()

    context = {
        'category_list': category_list,
    }

    return context
