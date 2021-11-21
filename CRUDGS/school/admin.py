from django.contrib import admin
from school import models


@admin.register(models.User)
class Admin(admin.ModelAdmin):
  list_display=['id','name','email','password']
    

