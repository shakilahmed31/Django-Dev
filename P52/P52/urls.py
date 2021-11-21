
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fview/',views.StudentCreateView.as_view(),name='fview'),
    path('created/',views.ThankYou.as_view(),name='create'),
]
