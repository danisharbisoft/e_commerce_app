from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=80, null=False)
    product_description = models.CharField(max_length=500)
    product_price = models.IntegerField(null=False)
    product_image = models.ImageField(upload_to='product_images/')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.product_name
