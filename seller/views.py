from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from .forms import ProductForm, StoreForm



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
    return render(request, "index.html", context)


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

    return render(request,"createstore.html", store = False)



#view product
@login_required(login_url="login")
def view_products(request):
    products = Product.objects.filter(profile__user = request.user).all()
    store = Profile.objects.filter(user = request.user).first()

    context = { 'products':products, 'store': store}
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
    context ={ 'store': store.first()}
    return render(request,"add_product.html", context)


#edit product
@login_required(login_url='login')
def edit_products(request, product_id):
    store = Profile.objects.filter(user = request.user).first()
    products = Product.objects.filter(profile__user = request.user).all()
    get_product = Product.objects.get(pk = product_id)
    form = ProductForm(instance=get_product)
     
    if request.method == 'POST':
        if get_product in products:
            form = ProductForm(request.POST, request.FILES, instance = get_product)
            if form.is_valid():
                form.save()
            messages.success(request, "Changes saved.")
            return redirect("products")
            
            
        else:
            messages.error(request, "Unauthorized Access")
            return redirect("products")

    context = {
        'product':get_product,
        'form':form, 'store':store
    }
    
    return render(request, 'edit_product.html', context)

#delete product
@login_required(login_url='login')
def delete_product(request, product_id):
    product = Product.objects.get(pk = product_id)
    product.delete()
    messages.success(request, "Item deleted")
    return redirect("products")


#edit store
@login_required(login_url='login')
def edit_store(request, profile_id):
    store = Profile.objects.get(pk = profile_id)

    if store:
        form = StoreForm(instance=store)

        if request.method == 'POST':
            form = StoreForm(request.POST, request.FILES, instance=store)
            if form.is_valid():
                form.save()
            messages.success(request, "CHanges saved")
            return redirect("dashboard")

        context = {
            'store':store,
            'form':form
        }

        return render(request, 'edit_store.html', context)

    else:
        return redirect("createstore")



#view store for (USER & SELLER)
def store(request, profile_name):
    get_store = Profile.objects.filter(name = profile_name )

    if get_store.exists():
        get_store = get_store.first()
        products = Product.objects.filter(profile = get_store).all()


        context= {
            'store': get_store,
            'products':products
        }
        return  render(request, "store.html", context)

    else:
        messages.error(request, "The store does not exist")
        return redirect("home")




    
# delete store
@login_required(login_url='login')
def delete_store(request, store_id):
    store = Profile.objects.get(pk=store_id)
    store.delete()
    messages.success(request, "store deleted")
    return redirect("Dashboard")



#shoplink (view product)
#user
#view product
#reviews
#ratings