
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('std/', views.student_view),
    path('thr/', views.teacher_view),
    path('sign/', views.sign_up),
]
