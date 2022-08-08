from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('settings/contactdetails', views.personal_details, name="personal_details"),

]