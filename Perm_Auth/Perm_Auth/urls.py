from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_signup,name='signup'),
    path('login/', views.user_login,name='login'),
    path('dashboard/', views.user_dashboard,name='dashboard'),
    path('logout/', views.user_logout,name='logout'),
    
]
