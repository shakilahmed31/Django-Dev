
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/',views.setcookie,name='set'),
    path('get/',views.getcookie,name='get'),
    path('del/',views.delcookie,name='del'),
]
