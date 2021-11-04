from django.contrib import admin
from . models import ExamCenter,Students

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
  list_display=['id','cname','city']
    

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
  list_display=['id','cname','city','name','roll']

