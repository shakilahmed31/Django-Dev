from django.db import models


class Students(models.Model):

  stuid   =models.IntegerField()
  stuname =models.CharField(max_length=30)
  stuemail=models.EmailField(max_length=30)
  stupass =models.CharField(max_length=30)
  
   