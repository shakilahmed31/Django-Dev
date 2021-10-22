
from django.contrib import admin
from django.urls import path ,include
from app1 import views as v1
from app2 import views as v2
from app3 import views as v3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('a4/',include('app4.urls')),
    path('a1/',v1.app1_func),
    path('a2/',v2.func),
    path('a3/',v3.Func3),
    
]
