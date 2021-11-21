
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup,name='signup'),
    path('login/', views.login_view,name='login'),
    path('profile/', views.profile_view,name='profile'),
    path('logout/', views.logout_view,name='logout'),
    path('changepass/', views.change_pass,name='changepass'),
    path('profilechange/', views.change_profile,name='profilechange'),
]