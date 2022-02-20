from .models import Category


def all_categories(request):
    """ View to return categories to the context"""

    category_list = Category.objects.all()

    context = {
        'category_list': category_list,
    }

    return context
