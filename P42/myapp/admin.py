from django.contrib import admin
from . models import Page,Song,Post

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
  list_display=['user','page_name','page_cat','page_publish_date']
    
@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
  list_display=['user','post_title','post_cat','post_publish_date']
    

@admin.register(Song)
class PageAdmin(admin.ModelAdmin):
   list_display=['song_name','song_duration','written_by']