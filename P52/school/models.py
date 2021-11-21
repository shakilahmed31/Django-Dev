
from django.db import models
from django.urls import reverse

class Student(models.Model):
  name=models.CharField(max_length=20)
  email=models.EmailField(max_length=20)
  password=models.CharField(max_length=10)

  def get_absolute_url(self):
      return reverse ("created")
  
