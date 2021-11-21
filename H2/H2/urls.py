from django.contrib import admin
from django.urls import path , include
from django.conf import Settings, settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecom/',include('ecom.urls')),
    path('blog/',include('blog.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
