
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.show_user_data),
    path('song/', views.show_song_data,name='song'),
    path('post/', views.show_post_data,name='post'),
    path('page/', views.show_page_data,name='page'),
    path('',views.home_view,name='user'),
]
