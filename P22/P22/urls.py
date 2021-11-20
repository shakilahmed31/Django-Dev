
from django.contrib import admin
from django.urls import path
from paschk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regi/', views.student_view),
]
