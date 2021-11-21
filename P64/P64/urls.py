
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.thankyou,name='test'),
    path('logout/',views.user_logout,name='logout'),
    path('changepass/',views.user_changepass,name='changepass'),
    path('changepass1/',views.user_changepass1,name='changepass1'),
    path('userprofile/',views.user_profile,name='userprofile'),
]
