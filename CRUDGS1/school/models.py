from django.db import models

class StudentRegistration(models.Model):
  name=models.CharField(max_length=20)
  roll=models.IntegerField()
  email=models.EmailField(max_length=20)
  password=models.CharField(max_length=10)
