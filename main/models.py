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






