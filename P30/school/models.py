from django.db import models

class Student(models.Model):
  name=models.CharField(max_length=20)
  roll=models.IntegerField(unique=True,null=False)
  city=models.CharField(max_length=30)
  marks=models.IntegerField()
  pass_date=models.DateField()

