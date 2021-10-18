
from django.contrib import admin
from django.urls import path,include
from app1 import views
from app3 import views as v1

apppattern = [

    path('appdj/',include('app1.urls')),
    path('apppy/',views.Learnpy),


]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(apppattern)),
    path('ap2/',include('app2.urls')),
    path('ap3/',include([

        path('feed/',v1.Django_fee),
        path('feep/',v1.Python_fee)

    ]))
]
