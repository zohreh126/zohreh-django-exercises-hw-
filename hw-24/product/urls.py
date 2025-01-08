from django.urls import path
from . import views 

urlpatterns = [
    path("product/", views.product_show, name="products page")
]
