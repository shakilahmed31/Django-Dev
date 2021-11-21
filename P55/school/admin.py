from django.contrib import admin
from django.db import models
from . models import Student
    
@admin.register(Student)
class StidentAdmin(admin.ModelAdmin):
  list_display=['id','name','email','password']
