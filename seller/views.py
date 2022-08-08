from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *



def home(request):
    context = {}
    return render(request, "home.html", context)


@login_required(login_url='login')
def personal_details(request):
    context = {}
    return render(request, "account/profile.html", context)

#dashboard
@login_required(login_url="login")
def dashbaord(request):
    shop = Profile.objects.filter(user = request.user)
    if shop.exists():
        shop = shop.first()
    else:
        shop = False

    context={shop:'shop'}
    return render(request, "dashboard.html", context)


#create shop
@login_required(login_url="login")
def create_shop(request):
    pass


#view product
@login_required(login_url="login")
def view_products(request):
    products = Product.objects.filter(profile = " ")
    context = {}
    return render(request, "prdouct.html", context)


#add product
#edit product



#shoplink (view product)
