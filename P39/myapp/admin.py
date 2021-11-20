from django.contrib import admin
from . models import Page

@admin.register(Page)
class UserAdmin(admin.ModelAdmin):
  list_display=['user','page_name','page_cat','page_publish_date']
    


