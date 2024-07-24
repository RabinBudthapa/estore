from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    logo=models.CharField(max_length=200,blank=True)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    def __str__(self):
        return self.name

class Slider(models.Model):
    name=models.CharField(max_length=500)
    image=models.ImageField(upload_to='media')
    description=models.TextField(blank=True)
    rank=models.IntegerField()
    url=models.URLField(blank=True,max_length=500)
    def __str__(self):
       return self.name

class Ad(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    description=models.TextField()
    rank=models.IntegerField()
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    rank=models.IntegerField()
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)
    def __str__(self):
        return self.name
STOCK=(('in_stock','In_Stock'),('out of stock','Out of Stock'))
LABELS=(('','default'),('new','new'),('sale','sale'),('hot','hot'))
class Product(models.Model):
    name = models.CharField(max_length=500)
    price=models.IntegerField()
    discounted_price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='media')
    description=models.TextField(blank=True)
    specification=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock = models.CharField(choices=STOCK,max_length=50)
    labels=models.CharField(choices=LABELS,max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)

    def __str__(self):
        return self.name
class CustomerReview(models.Model):
    name=models.CharField(max_length=500)
    post=models.CharField(max_length=500)
    image=models.ImageField(upload_to='media')
    comment=models.TextField(max_length=500,blank=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    username = models.CharField(max_length=300)
    slug = models.CharField(max_length=500)
    quantity = models.FloatField()
    total = models.FloatField()
    items = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    checkout = models.BooleanField(default=False)
    grandtotal = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.username

class Wishlist(models.Model):
    username = models.CharField(max_length=300)
    slug = models.CharField(max_length=500)
    items = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    checkout = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class ProductReview(models.Model):
    username = models.CharField(max_length=300)
    slug = models.CharField(max_length=500)
    star = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class OrderDetail(models.Model):
    ORDER_STATUS = (
        ("Order Received", "Order Received"),
        ("Order Processing", "Order Processing"),
        ("On the way", "On the way"),
        ("Order Completed", "Order Completed"),
        ("Order Canceled", "Order Canceled"),
    )

    PAYMENT_CHOICES = [
        ('Khalti', 'Khalti'),
        ('Cash On Delivery', 'Cash On Delivery'),
    ]
    username = models.CharField(max_length=300)
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    phone_number = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default="Cash On Delivery")
    total = models.PositiveIntegerField(default=10)
    payment_completed = models.BooleanField(default=False, null=True, blank=True)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS,default="Order Processing")


    def __str__(self):
        return self.username

class OrderItem(models.Model):
    order = models.ForeignKey(OrderDetail,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=500)
    price = models.CharField(max_length=500)


    def __str__(self):
        return self.order.user.username

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.name










