from django.db import models

class ExamCenter(models.Model):
  cname=models.CharField(max_length=20)
  city=models.CharField(max_length=10)

class Students(ExamCenter):
  name=models.CharField(max_length=20)
  roll=models.IntegerField()
