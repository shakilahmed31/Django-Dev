
from django.contrib import admin
from django.urls import path , include 
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView
from myapp.forms import LoginForm
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='myapp/home.html'),name='home'),
    path('dashboard/', TemplateView.as_view(template_name='myapp/dashboard.html'),name='dashboard'),
    path('login/',auth_view.LoginView.as_view(template_name='myapp/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
    path('changepass/',auth_view.PasswordChangeView.as_view(template_name='myapp/changepass.html',
    success_url='/changepassdone/'),name='changepass'),
    path('changepassdone/',auth_view.PasswordChangeDoneView.as_view(template_name='myapp/changepassdone.html')
    ,name='changepassdone'),
]

