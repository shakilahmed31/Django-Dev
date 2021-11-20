
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regi/',views.student_view),
    path('cong/',views.thank_view),
]
