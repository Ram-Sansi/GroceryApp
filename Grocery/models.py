from django.db import models
from django.utils.html import format_html


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    class Meta:
        db_table = 'category'

        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Merchant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    shop_name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)

    class Meta:
        db_table = 'Merchant'


    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(max_length=20)
    discount = models.IntegerField()
    image = models.FileField(upload_to='products/')

    Merchant = models.ForeignKey(to=Merchant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name_plural = 'products'
