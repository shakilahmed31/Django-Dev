
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home'),
    path('create',views.create_view,name='create'),
    path('del/<int:id>',views.del_view,name='del'),
    
]
