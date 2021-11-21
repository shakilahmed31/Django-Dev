from django.contrib import admin
from .models import Product



@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display=['product_id','product_name','desc','pub_date']

