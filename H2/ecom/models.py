from django.db import models

class Product(models.Model):
  product_id=models.AutoField
  product_name=models.CharField(max_length=30)
  category=models.CharField(max_length=50 , default="")
  subcategory=models.CharField(max_length=50 ,default="")
  price=models.IntegerField(default=0)
  desc=models.CharField(max_length=200)
  pub_date=models.DateField()
  image=models.ImageField(upload_to='ecom/images',default="")
