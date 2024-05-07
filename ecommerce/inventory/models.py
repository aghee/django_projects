from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    IN_STOCK="IS"
    OUT_OF_STOCK="OOS"
    BACKORDER="BO"

    STOCK_STATUS={
        IN_STOCK:"In stock",
        OUT_OF_STOCK:"Out of stock",
        BACKORDER:"Backordered"
    }

    pid=models.CharField(max_length=200)
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(null=False,unique=True)
    description=models.TextField(null=True)
    is_digital=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now=True,editable=False)
    is_active=models.BooleanField(default=False)
    stock_status=models.CharField(max_length=3, 
                                  choices=STOCK_STATUS, 
                                  default=OUT_OF_STOCK)
    category=models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)
    seasonal_event=models.ForeignKey("SeasonalEvents",on_delete=models.SET_NULL,null=True)

    #field not created, used to create association/link/through  table
    product_type=models.ManyToManyField("ProductType",related_name="product_type")

class ProductLine(models.Model):
    price=models.DecimalField(decimal_places=2,max_digits=10000)
    sku=models.UUIDField(default=uuid.uuid4)
    stock_qty=models.IntegerField(default=0)
    is_active=models.BooleanField(default=False)
    order=models.IntegerField()
    weight=models.FloatField()
    product=models.ForeignKey(Product,on_delete=models.PROTECT)

    #field not created, used to create a link/through/association table
    attribute_values=models.ManyToManyField("AttributeValue",related_name="attribute_values") 

class ProductImage(models.Model):
    name=models.CharField(max_length=100)
    alternative_text=models.CharField(max_length=100)
    url=models.ImageField()
    order=models.IntegerField()
    product_line=models.ForeignKey(ProductLine,on_delete=models.CASCADE)

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True)
    is_active=models.BooleanField(default=False)
    parent=models.ForeignKey("self",on_delete=models.PROTECT) #selfreferencing FK

class SeasonalEvents(models.Model):
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    name=models.CharField(max_length=100,unique=True)

class Attribute(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True)

class ProductType(models.Model):
    name=models.CharField(max_length=100)
    parent=models.ForeignKey('self',on_delete=models.CASCADE)

class AttributeValue(models.Model):
    attribute_value=models.CharField(max_length=100)
    attribute=models.ForeignKey(Attribute,on_delete=models.CASCADE)

class ProductLine_AttributeValue(models.Model):
    attribute_value=models.ForeignKey(AttributeValue,on_delete=models.CASCADE)
    product_line=models.ForeignKey(ProductLine,on_delete=models.CASCADE)

class Product_ProductType(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_type=models.ForeignKey(ProductType,on_delete=models.CASCADE)

class StockControl(models.Model):
    stock_quantity=models.IntegerField()
    name=models.CharField(max_length=100)
    stock_product=models.OneToOneField(Product,on_delete=models.CASCADE)

