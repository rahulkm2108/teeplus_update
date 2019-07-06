from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import render
from django.http import JsonResponse
from .models import category
from .models import products
from .models import customers
from .forms import Login
from .forms import Registration
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
# Create your views here.
@csrf_exempt
def login(request):
    uname = request.GET.get('username')
    password = request.GET.get('password')
    print(uname)
    users = customers.objects.get(Email=uname, Password=password)

    if users:
        return JsonResponse({'response': 'Success', 'user': users.FirstName})
    else:
        return JsonResponse({'response': 'Failed'})

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


def contact_us(request):
    return  render(request, 'contact_us/contact_us.html')

def cart(request):
    return render(request, 'cart/cart.html')


def get_product(request, CategoryName):
    category_name = CategoryName
    cat_id = category.objects.get(CategoryName=category_name)
    pro_info = products.objects.filter(categoryId_id=cat_id.id)
    return render(request, 'products/get_product.html', {'pro_info': pro_info, 'category_name':category_name})

def pro_desc(request, pro_id):
    pro_info = products.objects.get(id=pro_id)
    print(pro_info)
    return render(request, 'products/pro_desc.html')

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
