from django.contrib import admin

# Register your models here.

from .models import Product,Ecom_user_profile,Ecom_user

admin.site.register(Product)
admin.site.register(Ecom_user)
admin.site.register(Ecom_user_profile)