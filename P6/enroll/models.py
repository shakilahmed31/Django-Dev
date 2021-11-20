from django.db import models

class Student(models.Model):
  stuid   = models.IntegerField(default=True)
  stuname = models.CharField(max_length=70)
  stuemail= models.EmailField(max_length=50)
  stupass = models.CharField(max_length=50)

  def __str__(self ):
  
   return self.stuemail
 

