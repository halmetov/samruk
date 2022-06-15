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
    catalog = Catalog.objects.get(id=int(catalog_id))
    categories = Category.objects.filter(catalog__id=int(catalog_id))
    categories12 = Category.objects.filter(catalog__id=int(catalog_id)).count()
    search_value = request.GET.get('search', None)
    total = Product.objects.filter(category__categorytype__category__catalog__id=int(catalog_id)).count()
    limit_per_page = 9
    limit_per_page_2 = 4
    current_page = 1
    if request.GET.get('page',1):
        current_page = int(request.GET.get('page',1))

    print(current_page)
    page = 'catalog'
    start = (current_page-1) * limit_per_page
    stop = current_page * limit_per_page
    if search_value:
        products = Product.objects.filter(category__categorytype__category__catalog__id=int(catalog_id)).filter(title__contains=search_value)
    else:
        products = Product.objects.filter(category__categorytype__category__catalog__id=int(catalog_id))[start:stop]
    page_count = ceil(total * 1.0 / limit_per_page)
    pages = [i + 1 for i in range(page_count)]


    return render(request, 'shop-sidebar.html', {
        'catalog': catalog,
        'categories': categories,
        'products': products,
        'pages': pages,
        'current_page': current_page,
        'search_value': search_value,
        'categories12': categories12
    })


def shopcatHandler(request, cat_id):
    category = Category.objects.get(id=int(cat_id))
    category_types = CategoryType.objects.filter(category__id=int(cat_id))
    products = Product.objects.filter(category__categorytype__category__id=int(cat_id))
    return render(request, 'shop-category.html', {
        'category': category,
        'category_types': category_types,
        'products': products
    })


def shopcattypeHandler(request, cattype_id):
    categorytype = CategoryType.objects.get(id=int(cattype_id))
    category_sizes = CategorySize.objects.filter(categorytype__id=int(cattype_id))
    products = Product.objects.filter(category__categorytype__id=int(cattype_id))

    return render(request, 'shop-cat-type.html', {
        'categorytype': categorytype,
        'category_sizes': category_sizes,
        'products': products
    })

def shopcatsizeHandler(request, catsize_id):
    categorysize = CategorySize.objects.get(id=int(catsize_id))
    products = Product.objects.filter(category__id=int(catsize_id))

    return render(request, 'shop.html', {
        'categorysize': categorysize,
        'products': products
    })

