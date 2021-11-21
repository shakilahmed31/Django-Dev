
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.TemplateView.as_view(template_name='school/home.html'),name='blankhome'),
    path('home/',views.RedirectView.as_view(url='/Something/'),name='home'),
    #path('index/',views.RedirectView.as_view(url='/'),name='index'),
    path('bbc/',views.RedirectView.as_view(url='https://www.bbc.com'),name='bbc'),

    path('index/',views.RedirectView.as_view(pattern_name='home'),name='index'),
    path('cnn/',views.RedirectTest.as_view(),name='cnn'),

    path('home/<int:pk>',views.RedirectTest2.as_view(url=''),name='Rtest2'),
]
