from django.db import models

class CommonInfo(models.Model):
  name=models.CharField(max_length=20)
  age=models.IntegerField()
  date=models.DateField()

  class Meta:
    abstract=True

class Students(CommonInfo):
  fees=models.IntegerField()
  date=None
  
class Teacher(CommonInfo):
  salary=models.IntegerField()

class Contractor(CommonInfo):
  payment=models.IntegerField()
  date=models.DateTimeField()