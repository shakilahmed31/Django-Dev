from django.contrib import admin
from . models import Students


@admin.register(Students)
class Admin(admin.ModelAdmin):
  list_display=['stuid','stuname','stuemail','stupass']