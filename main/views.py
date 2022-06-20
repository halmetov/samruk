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
    cats = Catalog.objects.all()
    cates = Category.objects.all()
    services = Service.objects.all()
    products = Product.objects.all()
    new_products = Product.objects.filter(is_new=True)
    bs_products = Product.objects.filter(is_best_seller=True)
    sponsors = Sponsor.objects.all()
    blogs = Blog.objects.filter()
    mains = Main.objects.all()[:3]
    catalogs = Catalog.objects.all()[:3]


    return render(request, 'index-5.html', {
        'services': services,
        'cats': cats,
        'cates': cates,
        'products': products,
        'catalogs': catalogs,
        'new_products': new_products,
        'bs_products': bs_products,
        'sponsors': sponsors,
        'blogs': blogs,
        'mains': mains

    })


def blogHandler(request):
    cats = Catalog.objects.all()
    cates = Category.objects.all()
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
        'cats': cats,
        'cates': cates,

    })


def blog_detailHandler(request, blog_detail_id):
    cats = Catalog.objects.all()
    cates = Category.objects.all()
    blog_detail = Blog.objects.get(id=int(blog_detail_id))
    blog_quote = BlogQoute.objects.all()
    categories = BlogCategory.objects.filter()
    latest_blogs = Blog.objects.filter(is_latest=True)

    return render(request, 'blog-details.html', {
        'blog_detail': blog_detail,
        'categories': categories,
        'cats': cats,
        'cates': cates,
        'blog_quote': blog_quote,
        'latest_blogs': latest_blogs
    })



def aboutHandler(request):
    cats = Catalog.objects.all()
    cates = Category.objects.all()
    about = About.objects.all()
    staff = Staff.objects.all()
    comment = Comment.objects.all()
    statistics = Statistics.objects.all()
    return render(request, 'about-us.html', {
        'cats': cats,
        'cates': cates,
        'about': about,
        'staff': staff,
        'comment': comment,
        'statistics': statistics
    })


def contactHandler(request):
    if request.method == 'GET':
        contact = Contact.objects.all()
        cats = Catalog.objects.all()
        cates = Category.objects.all()
        return render(request, 'contact-us.html', {
            'contact': contact,
            'cats': cats,
            'cates': cates,
        })
    else:
        r = Register()
        last_name = request.POST.get('last_name', '')
        first_name = request.POST.get('first_name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        r.last_name = last_name
        r.first_name = first_name
        r.phone = phone
        r.email = email
        r.message = message
        r.save()

    return JsonResponse({'success': True, 'errorMsg': '', '_success': True})




def shopHandler(request, catalog_id):
    cats = Catalog.objects.all()
    cates = Category.objects.all()
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
        'cats': cats,
        'cates': cates,
        'colors': colors,
        'sort_key': sort_key
    })


def shopcatHandler(request, cat_id):
    cats = Catalog.objects.all()
    cates = Category.objects.all()
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
        'cats': cats,
        'cates': cates,
        'current_page': current_page,
        'search_value': search_value,
        'catalogs': catalogs,
        'colors': colors,
    })


def shopcattypeHandler(request, cattype_id):
    cats = Catalog.objects.all()
    cates = Category.objects.all()
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
        'cats': cats,
        'cates': cates,
        'colors': colors,
    })

def shopcatsizeHandler(request, catsize_id):
    cats = Catalog.objects.all()
    cates = Category.objects.all()
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
        'cats': cats,
        'cates': cates,
        'stop': stop,
        'total': total,
        'pages': pages,
        'current_page': current_page,
    })

def productHandler(request, pr_id):
    cats = Catalog.objects.all()
    cates = Category.objects.all()

    pr = Product.objects.get(id=int(pr_id))
    colors = Color.objects.all()
    sizes = Size.objects.all()

    return render(request, 'product-details-2.html', {
        'pr': pr,
        'colors': colors,
        'sizes': sizes,
        'cats': cats,
        'cates': cates,
    })
