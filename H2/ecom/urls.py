from django.urls import path
from ecom import views

urlpatterns = [
        path('',views.index,name='ecomhome'),
        path('about/',views.about,name='AboutUs'),
        path('contact/',views.contact,name='ContactUs'),
        path('tracker/',views.tracker,name='TrackingStatus'),
        path('search/',views.search,name='Search'),
        path('productview/',views.productview,name='Search'),
        path('checkout/',views.checkout,name='Checkout'),
]