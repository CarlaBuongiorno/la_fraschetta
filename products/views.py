from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """
        A view to show all products, including sorting and search queries.
        Also enables all categories to render in the menus.
    """

    products = Product.objects.all()
    category_list = Category.objects.all()
    query = None
    categories = None
    template_sort_key = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            product_sort_key = request.GET['sort']
            template_sort_key = product_sort_key
            if product_sort_key == 'name':
                product_sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if product_sort_key == 'category':
                product_sort_key = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    product_sort_key = f'-{product_sort_key}'
                products = products.order_by(product_sort_key)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__backend_name__in=categories)
            categories = Category.objects.filter(backend_name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{template_sort_key}_{direction}'

    context = {
        'products': products,
        'category_list': category_list,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
