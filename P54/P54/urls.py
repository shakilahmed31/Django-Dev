from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.display_view.as_view(),name='display'),
    path('create/',views.Student_View.as_view(),name='cr'),
    path('done/',views.ThankYou.as_view(),name='tks'),
    path('update/<int:pk>',views.UpdateView.as_view(),name='stuupdate'),
    path('delete/<int:pk>',views.StudentDeleteView.as_view(extra_context={'fm':'fm'}),name='studelete'),
]
