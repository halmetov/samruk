from django.db import models

# Create your models here.

class Catalog(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    is_main = models.BooleanField()

    def __str__(self):
        return self.title

class Category(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    is_main = models.BooleanField()
    pr_amount = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.title


class CategoryType(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    is_main = models.BooleanField()
    pr_amount = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title

class CategorySize(models.Model):
    categorytype = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    is_main = models.BooleanField()
    pr_amount = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=300)
    is_main = models.BooleanField()

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=300)
    is_main = models.BooleanField()
    code = models.CharField(max_length=100,blank=True)
    col_amount = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300)
    rating = models.FloatField(default= 0.0)
    views = models.IntegerField(default=0)
    short_description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(CategorySize, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    weight = models.CharField(max_length=100)
    description = models.TextField()
    details = models.TextField()
    logo = models.ImageField(upload_to='upload')
    discount = models.IntegerField(default=0)
    is_new = models.BooleanField()
    is_best_seller = models.BooleanField()
    kaspi_link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class Main(models.Model):
    title = models.CharField(max_length=300, blank=True)
    title1 = models.CharField(max_length=300, blank=True)
    main_info = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return self.title



class Service(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    description = models.TextField(blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class BlogCategory(models.Model):
    title = models.CharField(max_length=300)
    is_main = models.BooleanField(blank=True)
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title




class Blog(models.Model):
    which_one = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300, blank=True)
    main_description = models.CharField(max_length=300)
    more_description = models.TextField(blank=True)
    main_logo = models.ImageField(upload_to='upload')
    logo1 = models.ImageField(upload_to='upload', blank=True)
    logo2 = models.ImageField(upload_to='upload', blank=True)
    date = models.DateField()
    is_latest = models.BooleanField(blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    gmail = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)
    whatsapp = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title


class BlogQoute(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    description = models.TextField()
    action = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.first_name


class Sponsor(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    photo = models.ImageField(upload_to='upload')


    def _str_(self):
        return self.title


class Comment(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    description = models.TextField()
    photo = models.ImageField(upload_to='upload')

    def _str_(self):
        return self.first_name


class Statistics(models.Model):
    title = models.CharField(max_length=300)
    count = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')

    def _str_(self):
        return self.title

class Staff(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='upload')

    def _str_(self):
        return self.first_name


class Contact(models.Model):
    name = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)
    whatsapp = models.CharField(max_length=300, blank=True)
    time = models.CharField(max_length=300, blank=True)
    karta = models.CharField(max_length=300, blank=True)

    def _str_(self):
        return self.name


class Register(models.Model):
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    message = models.TextField()

    def _str_(self):
        return self.last_name




