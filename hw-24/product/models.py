from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name= models.CharField(max_length=50)

    def __str__(self):
        return f"name : {self.cat_name}"


class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    category=models.ManyToManyField(Category)

    def __str__(self):
        return f"name:{self.product_name} price:{self.product_price} "