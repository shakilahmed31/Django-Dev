from django.urls import path
from app2 import views

urlpatterns = [
    
    path('Learndji/',views.Learndj_int),
    path('Learnpyi/',views.Learnpy_int),
]