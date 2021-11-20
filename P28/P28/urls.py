
from django.contrib import admin
from django.urls import path
from applog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_auth_view),
]
