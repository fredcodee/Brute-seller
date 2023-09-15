from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('settings/profile/details', views.personal_details, name="profile_details"),
    path('dashboard', views.dashbaord, name="dashboard"),
    path('createstore', views.create_shop, name = 'createstore'),
    path('dashboard/products', views.view_products, name='products'),
    path('product/add', views.add_products, name="add_product" ),
    path('product/edit/<int:product_id>', views.edit_products, name="edit_product"),
    path("product/delete/<int:product_id>", views.delete_product, name="delete_product"),
    path('mystore/edit/<int:profile_id>', views.edit_store, name="edit_store"),
    path('store/<str:profile_name>', views.store, name='store'),
    path("store/delete/<int:store_id>", views.delete_store, name= "delete_store"),
    path('product/<str:profile_name>/<int:product_id>', views.view_product, name="product"),
    path('settings/general', views.settings, name="settings"),
    # path('payments', views.payments, name="payments"),
    path('product/order/<int:product_id>', views.order, name="order"),
]