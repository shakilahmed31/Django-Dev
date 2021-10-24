from django.contrib import admin
from . models import User



@admin.register(User)
class Admin(admin.ModelAdmin):
  list_display=['id','tname','sname','email','password']
    



