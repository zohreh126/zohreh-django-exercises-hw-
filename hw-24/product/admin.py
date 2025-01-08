from django.contrib import admin
from product.models import Category, Product
# Register your models here.



class AdminCategory(admin.ModelAdmin):
    list_display=[
        "cat_name"
    ]

class AdminProduct(admin.ModelAdmin):
    list_display=[
        "product_name","product_price", "Category_show"
    ]


    def Category_show (self, obj):
        for i in obj.category.all():
            return f"{i.cat_name}"


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)