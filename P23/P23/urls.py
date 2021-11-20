
from django.contrib import admin
from django.urls import path
from erchk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('r1/', views.stu_view),
]
