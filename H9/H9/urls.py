
from django.contrib import admin
from django.urls import path
from textutils import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze/',views.analyze,name='analyze'),
    #path('removepunc/',views.removepunc,name='removepunc'),
    path('vowel/',views.vowel,name='vowel'),
    path('vanz/',views.vanalyze,name='vanz'),

    path('capitalizefirst/',views.capfirst,name='capfirst'),
    path('newlineremove/',views.newlineremove,name='newlineremove'),
    path('spaceremover/',views.spaceremover,name='spaceremover'),
    path('charcount/',views.charcount,name='charcount'),
]
