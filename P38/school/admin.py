from django.contrib import admin
from .models import Students,ProxyStudent


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll']


@admin.register(ProxyStudent)
class ProxyAdmin(admin.ModelAdmin):
    list_display=['id','name','roll']




