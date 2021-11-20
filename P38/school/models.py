from django.db import models
from .managers import CustomManager

class Students(models.Model):
  name=models.CharField(max_length=20)
  roll=models.IntegerField()
  #objects=models.Manager() # default Manager  
  #stu=CustomManager()  # Customs manager
class ProxyStudent(Students):
  stu=CustomManager()
  class Meta:
    proxy=True 
    ordering=['name'] 