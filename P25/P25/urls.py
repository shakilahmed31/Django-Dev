
from django.contrib import admin
from django.urls import path
from durl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('np/<int:mid>/',views.show_data,name='details'),
    path('',views.home_view , name='etc'),
    path('np/<int:mid>/<int:msid>/',views.show_sub_data,name='sub_details'),
]
