
from django.contrib import admin
from django.urls import path
from appauth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup_view),
]

