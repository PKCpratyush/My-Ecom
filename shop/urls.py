# from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name="Shope_home"),
    path('login_page/',views.login, name="loginpage"),
    path('sign_up/',views.signup, name="sign_Up"),
    path('about/',views.about, name="about_us"),
    path('contact/',views.contact_us, name="contact_us"),
    path('search/',views.search, name="search"),
    path('product_view/',views.product_view, name="product_view"),
]
