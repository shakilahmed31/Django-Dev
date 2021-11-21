from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_date,name='home'),
    path('add/',views.add_data,name='add'),
    path('del/<id>',views.del_date,name='del'),
    path('update/<id>',views.update_data,name='update'),
]
