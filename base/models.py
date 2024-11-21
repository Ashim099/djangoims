from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class user(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=8)
    email = models.EmailField()
    image = models.FileField()
    address = models.CharField( max_length=50)
    contact = models.CharField(max_length=50)

class Productcategory(models.Model):
    product_category = models.CharField(max_length= 300)
    def __str__(self):
        return self.product_category
    
class Department(models.Model):
    name = models.CharField(max_length= 300)
    floor = models.IntegerField()
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=300)
    image = models.FileField()
    description = models.TextField()
    category = models.ForeignKey(Productcategory, on_delete = models.SET_NULL, null=True)
    department_name = models.ManyToManyField('Department',null=True,blank=True)
    stock = models.IntegerField()
    def __str__(self):
        return self.name


class vendor(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    
class purchase(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    vendor = models.ForeignKey(vendor, on_delete=models.SET_NULL, null=True)

class sell(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    customer_number = models.CharField(max_length=300)

    
    


