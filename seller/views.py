from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def home(request):
    context = {}
    return render(request, "home.html", context)


@login_required(login_url='login')
def personal_details(request):
    context = {}
    return render(request, "account/profile.html", context)

