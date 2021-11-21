
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.addandshow,name='home'),
    path('del/<int:id>',views.student_del,name='del'),
    path('update/<int:id>',views.student_update,name='update')
   
]
