from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('settings/contactdetails', views.personal_details, name="personal_details"),
    path('dashboard', views.dashbaord, name="dashboard"),
    path('createstore', views.create_shop, name = 'createstore'),
    path('dashboard/products', views.view_products, name='products'),
    path('product/add', views.add_products, name="add_product" ),
]