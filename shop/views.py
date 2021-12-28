from django.db.models.fields import AutoField
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Ecom_user,Ecom_user_profile
from datetime import datetime
import uuid



from math import ceil

# Create your views here.

# super user name: mr_pkc; pass: password

def number_of_slides(number_of_products):
    return number_of_products//4 + ceil((number_of_products/4) - (number_of_products//4))


def index(request):
    products = Product.objects.all()
    length = len(products)
    # number_of_slides = length//4 + ceil((length/4) - (length//4))
    product_categories = {}
    for i in products:
        if i.product_category in product_categories:
            product_categories[i.product_category].append(i)
        else:
            product_categories[i.product_category] = [i]

    for category,categorised_product in product_categories.items():
        product_categories[category] = [categorised_product,range(1,number_of_slides(len(categorised_product)))]
        # print(d[i])

    # product_data = {"number_of_slides":number_of_slides,"products": products, "range":range(1,length)}
    product_data = {"products":product_categories}
    return render(request, "shop/index.html",product_data)

def authorization_check(user_name, user_password):
    return Ecom_user.objects.filter(user_name=user_name, user_password=user_password).exists()

def login(request):
    user_name = request.POST.get("user_name","")
    user_password = request.POST.get("user_password","")
    if user_name == "" and user_password == "":
        return render(request, 'shop/login_page.html', {"check_empty_field":False, "message":"Refresh Page"})

    elif user_name == "" or user_password == "":
        return render(request, 'shop/login_page.html', {"check_empty_field":True, "message":"Don't leave any field blank"})

    if authorization_check(user_name, user_password):
        return render(request, "shop/index.html")

    return render(request, 'shop/login_page.html', {"check_empty_field":True, "message":"User doesn't exist"})

def signup(request):
    a = 0
    user_name = request.POST.get("user_name","")
    if user_name == "":
        return render(request, "shop/signup.html")
    user_password = request.POST.get("user_password","")
    user_first_name = request.POST.get("user_first_name","")
    user_last_name = request.POST.get("user_last_name","")
    user_gender = request.POST.get("user_gender","")
    user_aadhar = request.POST.get("user_aadhar", 99)
    user_date_joined = request.POST.get("user_date_joined", datetime.now())
    user = Ecom_user_profile(first_name = user_first_name, last_name = user_last_name, gender = user_gender,aadhar_uid =int(user_aadhar),date_joined = user_date_joined)
    user.save()

    user_profile = Ecom_user(user_password=user_password, user_name=user_name)
    user_profile.save()
    
    return render(request, "shop/index.html")

def about(request):
    return render(request, 'shop/about.html')

def search(request):
    pass

def contact_us(request):
    pass

def product_view(request):
    pass