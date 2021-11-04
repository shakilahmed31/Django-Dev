from django.db import models


class User(models.Model):
  sname=models.CharField(max_length=30)
  tname=models.CharField(max_length=30)
  email=models.EmailField(max_length=30)
  password=models.CharField(max_length=30)
  

