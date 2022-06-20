import datetime
from math import ceil
from django.shortcuts import render
from main.models import *
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.

def indexHandler(request):
    return render(request, 'index-5.html', {
    })


def aboutHandler(request):
    return render(request, 'about-us.html', {
    })


def contactHandler(request):
    return render(request, 'contact-us.html', {
    })


def shopHandler(request, catalog_id):
    sort_key = request.GET.get('sort_key', 'id')
    # orderby_values = {
    #     'popular': 'is_best_seller',
    #     'new': 'is_new',
    #     'dewevprice': 'new_price',
    #     'dorogprice': 'new_price',
    #     'reyting': ' rating'
    # }
    #
    # orderby_value = orderby_values.get(sort_key, 'id')

    catalog = Catalog.objects.get(id=int(catalog_id))
    categories = Category.objects.filter(catalog__id=int(catalog_id))
    for a in categories:
        a.pr_amount = Product.objects.filter(category__categorytype__category__id=int(a.id)).count()
    colors = Color.objects.all()
    for a in colors:
        a.col_amount = Product.objects.filter(color__id=int(a.id)).count()

    search_value = request.GET.get('search', None)

    total = Product.objects.filter(category__categorytype__category__catalog__id=int(catalog_id)).count()
    limit_per_page = 3
    limit_per_page_2 = 4
    current_page = 1
    if request.GET.get('page',1):
        current_page = int(request.GET.get('page',1))

    page = 'catalog'
    start = (current_page-1) * limit_per_page
    stop = current_page * limit_per_page
    if search_value:
        products = Product.objects.filter(title__contains=search_value)[start:stop]
    else:
        products = Product.objects.filter(category__categorytype__category__catalog__id=int(catalog_id)).order_by('-new_price')[start:stop]
    page_count = ceil(total * 1.0 / limit_per_page)
    pages = [i + 1 for i in range(page_count)]

    catalogs = Catalog.objects.all()
    start2 = start+1

    return render(request, 'shop-sidebar.html', {
        'catalog': catalog,
        'categories': categories,
        'products': products,
        'start': start2,
        'stop': stop,
        'total': total,
        'pages': pages,
        'current_page': current_page,
        'search_value': search_value,
        'catalogs': catalogs,
        'colors': colors,
        'sort_key': sort_key
    })


def shopcatHandler(request, cat_id):
    category = Category.objects.get(id=int(cat_id))
    category_types = CategoryType.objects.filter(category__id=int(cat_id))

    for a in category_types:
        a.pr_amount = Product.objects.filter(category__categorytype__id=int(a.id)).count()
    colors = Color.objects.all()
    for a in colors:
        a.col_amount = Product.objects.filter(color__id=int(a.id)).count()

    search_value = request.GET.get('search', None)

    total = Product.objects.filter(category__categorytype__category__id=int(cat_id)).count()
    limit_per_page = 3
    limit_per_page_2 = 4
    current_page = 1
    if request.GET.get('page', 1):
        current_page = int(request.GET.get('page', 1))

    page = 'catalog'
    start = (current_page - 1) * limit_per_page
    stop = current_page * limit_per_page
    if search_value:
        products = Product.objects.filter(title__contains=search_value)[start:stop]
    else:
        products = Product.objects.filter(category__categorytype__category__id=int(cat_id)).order_by(
            '-new_price')[start:stop]
    page_count = ceil(total * 1.0 / limit_per_page)
    pages = [i + 1 for i in range(page_count)]

    catalogs = Catalog.objects.all()
    start2 = start + 1


    return render(request, 'shop-category.html', {
        'category': category,
        'category_types': category_types,
        'products': products,
        'start': start2,
        'stop': stop,
        'total': total,
        'pages': pages,
        'current_page': current_page,
        'search_value': search_value,
        'catalogs': catalogs,
        'colors': colors,
    })


def shopcattypeHandler(request, cattype_id):
    categorytype = CategoryType.objects.get(id=int(cattype_id))
    category_sizes = CategorySize.objects.filter(categorytype__id=int(cattype_id))

    for a in category_sizes:
        a.pr_amount = Product.objects.filter(category__id=int(a.id)).count()
    colors = Color.objects.all()
    for a in colors:
        a.col_amount = Product.objects.filter(color__id=int(a.id)).count()

    search_value = request.GET.get('search', None)

    total = Product.objects.filter(category__categorytype__id=int(cattype_id)).count()
    limit_per_page = 3
    limit_per_page_2 = 4
    current_page = 1
    if request.GET.get('page', 1):
        current_page = int(request.GET.get('page', 1))

    page = 'catalog'
    start = (current_page - 1) * limit_per_page
    stop = current_page * limit_per_page
    if search_value:
        products = Product.objects.filter(title__contains=search_value)[start:stop]
    else:
        products = Product.objects.filter(category__categorytype__id=int(cattype_id)).order_by(
            '-new_price')[start:stop]
    page_count = ceil(total * 1.0 / limit_per_page)
    pages = [i + 1 for i in range(page_count)]

    catalogs = Catalog.objects.all()
    start2 = start + 1


    return render(request, 'shop-cat-type.html', {
        'categorytype': categorytype,
        'category_sizes': category_sizes,
        'products': products,
        'start': start2,
        'stop': stop,
        'total': total,
        'pages': pages,
        'current_page': current_page,
        'search_value': search_value,
        'catalogs': catalogs,
        'colors': colors,
    })

def shopcatsizeHandler(request, catsize_id):
    categorysize = CategorySize.objects.get(id=int(catsize_id))
    products = Product.objects.filter(category__id=int(catsize_id))


    total = Product.objects.filter(category__id=int(catsize_id)).count()
    limit_per_page = 3
    limit_per_page_2 = 4
    current_page = 1
    if request.GET.get('page', 1):
        current_page = int(request.GET.get('page', 1))

    page = 'catalog'
    start = (current_page - 1) * limit_per_page
    stop = current_page * limit_per_page

    products = Product.objects.filter(category__id=int(catsize_id)).order_by('-new_price')[start:stop]
    page_count = ceil(total * 1.0 / limit_per_page)
    pages = [i + 1 for i in range(page_count)]
    start2 = start + 1


    return render(request, 'shop.html', {
        'categorysize': categorysize,
        'products': products,
        'start': start2,
        'stop': stop,
        'total': total,
        'pages': pages,
        'current_page': current_page,
    })

