from django.db import models


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    dob = models.DateField()
    mobile = models.IntegerField()
    password = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)

    class Meta:
        db_table = 'client'
