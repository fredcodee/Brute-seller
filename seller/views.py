import profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages



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
    store = Profile.objects.filter(user = request.user).first()
    
    context={'store':store,}
    return render(request, "dashboard.html", context)


#create shop
@login_required(login_url="login")
def create_shop(request):
    if request.method =='POST':
        name = request.POST['name']
        bio =  request.POST['bio']

        #create store (user can only have one store)
        store  = Profile.objects.filter(user = request.user)
        if not store:
            new_store = Profile(user = request.user, name = name, bio = bio)
            new_store.save()

            messages.success(request, "You Have created your store.")
            return redirect("dashboard")

    return render(request,"createstore.html")



#view product
@login_required(login_url="login")
def view_products(request):
    products = Product.objects.filter(profile__user = request.user)
    context = { 'products':products}
    return render(request, "products.html", context)


#add product
@login_required(login_url="login")
def add_products(request):
    store  = Profile.objects.filter(user = request.user)
    if request.method =='POST':
        title = request.POST['title']
        description = request.POST['description']
        price =  request.POST['price']
        stock = request.POST['stock']

        #create product
        if store:
            new_product = Product(profile = store.first(), name=  title, description = description, stock = int(stock), price = float(price))
            new_product.save()

            messages.success(request, "You Have Added a product.")
            return redirect("products")
        else:
            messages.error(request, "You have no current store")
            return redirect("dashboard")
    return render(request,"add_product.html")


#edit product


#view store
#shoplink (view product)