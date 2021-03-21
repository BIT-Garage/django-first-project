from .import views
from django.urls import path



urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('blog_home',views.blog_home, name='about'),
    path('blog_single',views.blog_single, name='blog_single'),
    path('contact',views.contact, name='contact'),
    path('elements',views.elements, name='elements'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('price',views.price, name='price'),
    path('services',views.services, name='services'),


]
