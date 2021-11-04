from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
  #user=models.ForeignKey(User,on_delete=models.CASCADE)
  user=models.ForeignKey(User,on_delete=models.PROTECT)
  post_title=models.CharField(max_length=20)
  post_cat=models.CharField(max_length=20)
  post_publish_date=models.DateField()


