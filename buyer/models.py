from django.db import models
from django.contrib.auth.models import User
from seller.models import ProductModel


class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)


class ShippingDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, default='Your name ')
    city = models.CharField(max_length=70, null=False, default='Your city')
    address = models.CharField(max_length=200, null=False, default='Your address')
    email = models.EmailField(default='Your email')
