from school import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',views.Student_View.as_view(),name='cr'),
    path('done/',views.ThankYou.as_view(),name='tks'),
    path('update/<int:pk>',views.UpdateView.as_view(),name='stuupdate'),
    path('delete/<int:pk>',views.StudentDeleteView.as_view(),name='studelete'),
]
