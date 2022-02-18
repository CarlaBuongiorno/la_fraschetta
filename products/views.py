from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Avg

from .models import Product, Category
from .forms import ProductForm, CategoryForm
from reviews.models import Review
from reviews.forms import ReviewForm
from profiles.models import UserProfile
from wishlist.models import WishList


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

    reviews = Review.objects.all().filter()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']

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

    wishlist = None
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        wishlist = WishList.objects.filter(user_profile=user)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'avg_rating': avg_rating,
        'reviews': reviews,
        'user': user,
        'wishlist': wishlist,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all().filter(product=product)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    if not request.user.is_authenticated:
        template = 'products/product_detail.html'
        context = {
            'product': product,
            'reviews': reviews,
            'avg_rating': avg_rating,
        }
        return render(request, template, context)

    else:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        # find a match to the product and user
        wishlist = WishList.objects.filter(user_profile=user_profile, product=product_id)

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                reviews.create(
                    user_profile=user_profile,
                    product=product,
                    rating=request.POST.get('rating'),
                    review=request.POST.get('review'))
                messages.success(request, 'Successfully added review.')
                return redirect(reverse('product_detail', args=[product_id]))
            else:
                messages.error(request, 'Failed to add review. \
                        Please check the form is valid and try again.')
        else:
            form = ReviewForm()

        template = 'products/product_detail.html'
        context = {
            'form': form,
            'product': product,
            'user_profile': user_profile,
            'reviews': reviews,
            'avg_rating': avg_rating,
            'wishlist': wishlist,
        }

        return render(request, template, context)


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_category(request):
    """Add a category to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Successfully added category!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to add category. Please ensure the form is valid.')
    else:
        form = CategoryForm()
    template = 'products/add_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
