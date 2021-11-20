
from django.contrib import admin
from django.urls import path
from Modelform import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lp/', views.show_view),
]
