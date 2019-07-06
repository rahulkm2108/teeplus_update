"""Ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from EcommApp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.dashboard, name='dashboard'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('cart_page', views.cart, name='cart'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('registration', views.registration, name='registration'),
    path('products/get_product_category/<CategoryName>', views.get_product, name='get_product'),
    path('login', views.login, name='login'),
    path('wishlistData', views.wishlistData, name='wishlistData'),
    # url(r'^products/get_product_category/<CategoryName>', views.get_product, name='get_product'),
    path('products/pro_desc/<pro_id>', views.pro_desc, name='pro_desc'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view())
]
