from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import render
from django.http import JsonResponse
from .models import category
from .models import products
from .models import customers
from .models import cart
from .forms import Login
from .forms import Registration
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.http import HttpResponseRedirect
# Create your views here.
@csrf_exempt
def login(request):
    uname = request.GET.get('username')
    password = request.GET.get('password')
    print(uname)
    users = customers.objects.get(Email=uname, Password=password)

    if users:
        return JsonResponse({'response': 'Success', 'user': users.FirstName, 'id': users.id})
    else:
        return JsonResponse({'response': 'Failed'})

@csrf_exempt
def wishlistData(request):
    id = request.GET.get('userId')
    data = cart.objects.filter(customerId_id=id)
    wishlist_data = []
    for item in data:
        if item.wshishlist == 1:
            pro_info = products.objects.filter(id=item.productId_id).values()
            wishlist_data.append(pro_info[0])
            # print(pro_info[0].id)
    # print(wishlist_data)
    if data:
        return JsonResponse({'response': 'Success', 'data': wishlist_data})
    else:
        return JsonResponse({'response': 'Failed'})


def wishlistCount(request):
    id = request.GET.get('userId')
    wishcount = cart.objects.filter(customerId_id=id, wshishlist=1)
    cartcount = cart.objects.filter(customerId_id=id, cart=1)
    # print(len(wishcount))
    return JsonResponse({'response': 'Success', 'wishcount': len(wishcount), 'cartcount': len(cartcount)})


def updateWishlist(request):
    id = request.GET.get('id')
    loggedUserId = request.GET.get('loggedUserId')
    update = cart.objects.get(id=id)
    update.wshishlist = 0
    update.save()
    wishlist_info = cart.objects.filter(customerId_id=loggedUserId)
    wishlist_data = []
    for item in wishlist_info:
        if item.wshishlist == 1:
            pro_info = products.objects.filter(id=item.productId_id).values()
            wishlist_data.append(pro_info[0])
            # print(pro_info[0].id)
    # print(wishlist_data)
    return JsonResponse({'response': 'Success', 'data': wishlist_data})


def AddWishlist(request):
    id = request.GET.get('ProductId')
    CustomerId = request.GET.get('loggedUserId')
    WishlistCheck = cart.objects.filter(customerId_id=CustomerId, productId_id=id, wshishlist=1)
    wishcount = len(WishlistCheck)
    if wishcount > 0:
        return JsonResponse({'response': 'Failed'})
    else:
        checkUpdateWishlist = cart.objects.filter(customerId_id=CustomerId, productId_id=id, wshishlist=0)
        if len(checkUpdateWishlist) > 0:
            updateWish = cart.objects.get(customerId_id=CustomerId, productId_id=id, wshishlist=0)
            updateWish.wshishlist = 1
            updateWish.save()
            cartInfo = cart.objects.filter(customerId_id=CustomerId, wshishlist=1).values()
        else:
            cartAdd = cart(cart=0, wshishlist=1, customerId_id=CustomerId, productId_id=id)
            cartAdd.save()
            cartInfo = cart.objects.filter(customerId_id=CustomerId, wshishlist=1).values()

    return JsonResponse({'response': 'Success', 'data': list(cartInfo)})


def AddToCart(request):
    id = request.GET.get('ProductId')
    CustomerId = request.GET.get('loggedUserId')
    CartCheck = cart.objects.filter(customerId_id=CustomerId, productId_id=id, cart=1)
    cartcount = len(CartCheck)
    if cartcount > 0:
        return JsonResponse({'response': 'Failed'})
    else:
        checkUpdateCart = cart.objects.filter(customerId_id=CustomerId, productId_id=id, cart=0)
        if len(checkUpdateCart) > 0:
            updateCart = cart.objects.get(customerId_id=CustomerId, productId_id=id, cart=0)
            updateCart.cart = 1
            updateCart.save()
            cartInfo = cart.objects.filter(customerId_id=CustomerId, cart=1).values()
        else:
            cartAdd = cart(cart=1, wshishlist=0, customerId_id=CustomerId, productId_id=id)
            cartAdd.save()
            cartInfo = cart.objects.filter(customerId_id=CustomerId, cart=1).values()

    return JsonResponse({'response': 'Success', 'data': list(cartInfo)})


def dashboard(request):
    category.objects.all()
    info = category.objects.filter()
    # print(info)
    if request.method == 'POST':
        uname = request.POST.get('username')
        users = customers.objects.get(Email=uname)
        coockie =''
        if users:
            coockie = uname
        else:
            coockie = 'undefined'
        # print(users)
    form = Login()
    return render(request, 'dashboard/dashboard.html', {'data': info, 'form': form})
    return render(request, {'cookie_name': coockie})

@csrf_exempt
def getCartProduct(request):
    id = request.GET.get('id')
    cartInfo = cart.objects.filter(customerId_id=id, cart=1)
    proData = []
    for item in cartInfo:
        getProduct = products.objects.filter(id=item.id).values()
        proData.append(list(getProduct))

    return JsonResponse({'response': 'Success', 'data': proData})


def contact_us(request):
    return  render(request, 'contact_us/contact_us.html')

def cart_page(request):
    return render(request, 'cart/cart.html')

def wishlist(request):
    return render(request, 'wishlist/wishlist.html')

def get_product(request, CategoryName):
    category_name = CategoryName
    cat_id = category.objects.get(CategoryName=category_name)
    pro_info = products.objects.filter(categoryId_id=cat_id.id)
    return render(request, 'products/get_product.html', {'pro_info': pro_info, 'category_name':category_name})

def pro_desc(request, pro_id):
    pro_info = products.objects.get(id=pro_id)
    # print(pro_info)
    return render(request, 'products/pro_desc.html', {'data': pro_info})

def checkout(request):
    return render(request, 'checkout/checkout.html')

def registration(request):
    form = Registration()
    if request.method == 'POST':
        fname = request.POST.get('FirstName')
        lname = request.POST.get('LastName')
        email = request.POST.get('Email')
        number = request.POST.get('Number')
        password = request.POST.get('Password')
        cpassword = request.POST.get('ConfirmPassword')
        if password == cpassword:
            customer = customers(Email=email, Password=password, FirstName=fname, LastName=lname, PhoneNo=number, DOB='', Address='', Country='', State='', City='', PinCode=500008, Gender='', ProfileImg='', created='2019-01-01 00:00')
            customer.save()
    return render(request, 'registration/registration.html', {'form': form})
