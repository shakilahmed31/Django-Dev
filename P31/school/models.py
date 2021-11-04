from django.db import models

class Student(models.Model):
  name=models.CharField(max_length=20)
  roll=models.IntegerField(unique=True)
  city=models.CharField(max_length=20)
  marks=models.IntegerField()
  passdate=models.DateField()
  admdate=models.DateTimeField()

