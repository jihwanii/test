from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.forms import ImageField

# Create your models here.

####################################### USER ###########################################
class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    Phone_number = models.CharField(max_length=100,null=True)
    post_code = models.IntegerField(null = True)
    address = models.CharField(max_length=100,null=True)
    detail_address = models.CharField(max_length=100,null=True)


# class TimeStampedModel(models.Model):
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         abstract = True

class Seller(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    Phone_number = models.CharField(max_length=100,null=True)
    post_code = models.CharField(max_length=100,null=True)
    address  = models.CharField(max_length=100,null=True)
    detail_address = models.CharField(max_length=100,null=True)
    company_document = models.FileField(upload_to='media/', blank=True, null=True)



class Buyer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    Phone_number = models.CharField(max_length=100,null=True)
    post_code = models.CharField(max_length=100,null=True)
    address  = models.CharField(max_length=100,null=True)
    detail_address = models.CharField(max_length=100,null=True)
    company_document = models.FileField(upload_to='media/', blank=True, null=True)

###################################### Product #########################################

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Product(models.Model):
    user = models.ForeignKey(Seller, on_delete=models.CASCADE, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=50, null=True)
    MSRP = models.IntegerField()
    in_box = models.IntegerField()
    stock = models.IntegerField()
    barcode = models.IntegerField()
    image = models,ImageField(upload_to='media/', blank=True, null=True)
    content = models.TextField()
    product_document = models.FieldFile(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.product_name

