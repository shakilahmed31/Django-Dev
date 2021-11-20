
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.TemplateView.as_view(template_name='school/home.html'),name='blankhome'),
    path('home/',views.RedirectView.as_view(url='/'), name='home'),
    path('google/',views.RedirectView.as_view(url='https://www.google.com'), name='google'),
    path('googleV/',views.SelfDefine.as_view(), name='googleV'),
    path('index/',views.RedirectView.as_view(pattern_name='home'), name='index'),
    path('index/<int:pk>/',views.SelfDefine1.as_view(), name='goog'),
     path('<int:pk>/',views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),
]
