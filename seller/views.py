from multiprocessing import context
from django.shortcuts import render


def home(request):
    context = {}
    return render(request, "home.html", context)
