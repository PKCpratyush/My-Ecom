from django.utils.timezone import now
from django.db import models
from django.db.models.fields.related import ForeignKey
import uuid
# from django.contrib.postgres.fields import BigIntegerRangeField

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

# register your table in admin.py for using admin features

# db index
# date time field |/
# choices field |/
# text field |/

# class name should be uppercase

# UUID 

class Product(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4,unique=True)
    product_name = models.CharField(max_length=50)
    product_desription = models.TextField()
    publish_date = models.DateTimeField()
    product_category = models.CharField(max_length=40)
    product_price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to="shop/images", default = "")

    def __str__(self):
        return self.product_name


class Ecom_user_profile(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    phone_number = models.CharField(max_length=16)
    country_code = models.IntegerField(default=0)
    email = models.EmailField(default="")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to = "shop/user_images", default = "")
    gender = models.CharField(max_length=10)
    aadhar_uid = models.CharField(max_length=16)
    verification_status = models.CharField(max_length= 20, default="unverified")
    date_joined = models.DateTimeField(default=now())
    date_verified = models.DateTimeField(default=now())

class Ecom_user(models.Model):
    user_details = models.ForeignKey(Ecom_user_profile, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=16)
