from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length= 200, null=True, unique=True)
    bio = models.CharField(max_length=500, null=True)
    logo = models.ImageField(null = True, blank = True, upload_to = 'images/profiles')
    #product quality (average review)

    def __str__(self):
        return self.name

class Coins(models.Model):
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE, blank=True)
    btc = models.CharField(max_length=150, null = True)
    eth = models.CharField(max_length=150, null = True)


class Product(models.Model):
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE, blank=True)
    name = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=200, null=True)
    stock = models.IntegerField(default=0,null= True, blank=True)
    price = models.FloatField()
    image = models.ImageField(null = True, blank = True,upload_to = 'images/products')

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add= True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length= 200, null= True)
    quantity =  models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.transaction_id



class Ticket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    email =  models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=100, null= True)
    transaction_id = models.CharField(max_length= 200, null=True)
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
