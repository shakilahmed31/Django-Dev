from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fun/', views.homefun,name='fun'),
    path('funcl/', views.HomeClassView.as_view(),name='funcl'),
    path('about/', views.aboutfun,name='about'),
    path('aboutcl/', views.AboutClassView.as_view(),name='aboutcl'),
    path('contact/', views.contact_view,name='contact'),
    path('contactcl/', views.ContactClassView.as_view(),name='contactcl'),
    #path('news/', views.news,name='news'),
    path('news/', views.news,{'template_name':'school/news.html'},name='news'),
    path('news2/', views.news,{'template_name':'school/news2.html'},name='news2'),
    ###here template_name key pass it to view function and render ####
    path('newscl/', views.News.as_view(),name='newscl'),
    #path('newsclv/', views.News.as_view(),name='newsclv'),
    path('newsclv/', views.NewsClassView.as_view(template_name='school/news.html'),name='newsclv'),
    path('newsclv2/', views.NewsClassView.as_view(template_name='school/news2.html'),name='newsclv2'),
]
