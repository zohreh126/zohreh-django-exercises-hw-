from django.shortcuts import render
from .models import Product, Category
    # Create your views here.
    
def product_show(request):
    products=Product.objects.all()
    return render(request,'homepage.html' , {"products":products})