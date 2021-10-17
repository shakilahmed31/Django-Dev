
from django.contrib import admin
from django.urls import path
from testapp import views
from testapp.views import Test_func1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Test_func),
    path('Test_func1/', Test_func1),
]
