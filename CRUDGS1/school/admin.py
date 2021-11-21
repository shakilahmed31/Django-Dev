from django.contrib import admin
from .models import StudentRegistration


@admin.register(StudentRegistration)
class Admin(admin.ModelAdmin):
    list_display=['name','roll','email','password']

