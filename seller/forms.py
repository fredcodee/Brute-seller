from django.forms import ModelForm
from .models import *


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['profile']

class StoreForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user']

