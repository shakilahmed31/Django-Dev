
from django.urls import path
from .views import showdata, thankyou

urlpatterns = [
    path('sd/',showdata),
    path('success/',thankyou)
]
