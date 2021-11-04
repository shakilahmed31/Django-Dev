from django.db import models
from .managers import CustomManager

class Students(models.Model):
  name=models.CharField(max_length=20)
  roll=models.IntegerField()
  
  stu=CustomManager()