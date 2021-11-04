
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fv/',views.myview,name='fv'),
    #path('cv/',views.Myview.as_view(),name='cv'),
    path('cv/',views.Myview.as_view(name='Tahsin'),name='cv'),
    path('cc/',views.MyChildview.as_view(),name='cc'),
]
