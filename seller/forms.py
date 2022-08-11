from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import *


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['profile']