from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=10,null=True)
    email=models.EmailField(max_length=150,unique=True,verbose_name="email address",null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    # def __repr__(self):
    #     return self.first_name + " "+ self.last_name

    def __str__(self):
        return self.first_name + " "+ self.last_name


class Tag(models.Model):
    name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY=(
        ("Indoor","Indoor"),
        ("Out door","Out door"),
    )
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    description=models.CharField(max_length=100,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
        ("Pending","Pending"),
        ("Out for delivery","Out for delivery"),
        ("Delivered","Delivered"),
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=100,null=True,choices=STATUS)
    note=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.product.name
    
