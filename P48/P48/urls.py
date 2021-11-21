
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.StudentsView.as_view(),name='sudents'),
]
