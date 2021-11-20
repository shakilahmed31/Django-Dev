from django.db import models
from django.db.models.fields import proxy

class ExamCenter(models.Model):
  cname=models.CharField(max_length=20)
  city=models.CharField(max_length=20)

class MyExamCenter(ExamCenter):
  class Meta:
    proxy=True
    ordering=['city']
