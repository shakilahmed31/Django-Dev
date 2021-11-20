
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('changepass/',views.user_pass_change,name='changepass'),
]
