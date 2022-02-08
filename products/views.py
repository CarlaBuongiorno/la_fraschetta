from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
        A view to show all products, including sorting and search queries.
        Also enables all categories to render in the menus.
    """

    products = Product.objects.all()
    query = None
    categories = None
    template_sort_key = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            product_sort_key = request.GET['sort']
            template_sort_key = product_sort_key
            if product_sort_key == 'backend_name':
                product_sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('backend_name'))
            if product_sort_key == 'category':
                product_sort_key = 'category__backend_name'
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


def add_product(request):
    """Add a product to the store"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """Edit a product in the store"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    form = ProductForm(instance=product)
    messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
