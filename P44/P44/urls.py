
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', views.func_view,name='func'),
    path('clv/', views.class_view.as_view(),name='clv'),
    path('aboutfunc/',views.about,name='aboutfunc'),
    path('aboutcl/',views.About_view.as_view(),name='aboutcl'),
    path('form/',views.conttactform,name='form'),
    path('contact/',views.ContactForm.as_view(),name='contact'),
    #path('news/',views.news,name='news'),
    path('news/',views.news,{'tempalte_name':'school/news.html'},name='news'),

]
