from django.db import models

class Students(models.Model):
  name=models.CharField(max_length=20)
  roll=models.IntegerField()
  #objects=models.Manager()
  stu=models.Manager()