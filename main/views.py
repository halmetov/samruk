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
    services = Service.objects.all()
    products = Product.objects.all()
    new_products = Product.objects.filter(is_new=True)
    bs_products = Product.objects.filter(is_best_seller=True)
    sponsors = Sponsor.objects.all()
    blogs = Blog.objects.filter()
    mains = Main.objects.all()[:3]
    catalogs = Catalog.objects.all()[:2]


    return render(request, 'index-5.html', {
        'services': services,
        'products': products,
        'catalogs': catalogs,
        'new_products': new_products,
        'bs_products': bs_products,
        'sponsors': sponsors,
        'blogs': blogs,
        'mains': mains

    })


def blogHandler(request):
    which_one_id = int(request.GET.get('which_one_id', 0))

    limit = int(request.GET.get('limit', 2))
    current_page = int(request.GET.get('page', 1))
    stop = current_page * limit
    start = stop - limit

    if which_one_id:
        blogs = Blog.objects.filter(which_one__id=which_one_id)[start:stop]
        total = Blog.objects.filter(which_one__id=which_one_id).count()
    else:
        blogs = Blog.objects.filter()[start:stop]
        total = Blog.objects.count()

    prev_page = current_page - 1
    next_page = 0
    if total > stop:
        next_page = current_page + 1

    categories = BlogCategory.objects.filter()
    return render(request, 'blog.html', {
        'current_page': current_page,
        'prev_page': prev_page,
        'next_page': next_page,
        'total': total,
        'limit': limit,
        'blogs': blogs,
        'which_one_id': which_one_id,
        'categories': categories,

    })


def blog_detailHandler(request, blog_detail_id):
    blog_detail = Blog.objects.get(id=int(blog_detail_id))
    blog_quote = BlogQoute.objects.all()
    categories = BlogCategory.objects.filter()
    latest_blogs = Blog.objects.filter(is_latest=True)

    return render(request, 'blog-details.html', {
        'blog_detail': blog_detail,
        'categories': categories,
        'blog_quote': blog_quote,
        'latest_blogs': latest_blogs
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

