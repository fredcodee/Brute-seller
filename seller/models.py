from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length= 200, null=True, unique=True)
    bio = models.CharField(max_length=500, null=True)
    logo = models.ImageField(null = True, blank = True, upload_to = 'images/profiles', default = "images/profiles/profile.png")
    Stars = models.IntegerField(null= True, default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE, blank=True)
    name = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=200, null=True)
    stock = models.IntegerField(default=0,null= True, blank=True)
    price = models.FloatField()
    image = models.ImageField(null = True, blank = True,upload_to = 'images/products', default="images/products/product.png")

    def __str__(self):
        return self.name

class Order(models.Model):
    store=  models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank = False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add= True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length= 200, null= True)
    quantity =  models.IntegerField(default=0, null=True, blank=True)
    email = models.EmailField( null=True)
    coin = models.IntegerField(null = False, blank= False)

    def __str__(self):
        return self.transaction_id



class Ticket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    email =  models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=100, null= True)
    message = models.CharField(max_length=200, null= True)

    def __str__(self):
        return self.email

    

class Review(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length= 100, null=True)
    messeage  = models.CharField(max_length= 200, null=True)
    ratings  = models.IntegerField(default= 0 , null= True)

    def __str__(self):
        return self.name
