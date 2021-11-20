
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
     #path('',views.TemplateView.as_view(template_name='school/home.html'),name='home'),
     #path('',views.ChildClass.as_view(extra_context={'course':'Python'}),name='home'),
     path('home/<int:cl>',views.ChildClass.as_view(),name='cl'),
]
