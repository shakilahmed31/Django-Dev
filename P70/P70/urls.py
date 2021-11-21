
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/',views.myview,name='func'),
    path('cl/',views.MyView.as_view(name='Arosh'),name='cl'),
    path('subcl/',views.MyViewChild.as_view(),name='subcl'),
]
