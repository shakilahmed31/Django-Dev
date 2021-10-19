
from django.contrib import admin
from django.urls import path
from app1 import views
from app2.views import learnpy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj/',views.learndj),
    path('py/',learnpy),
]
