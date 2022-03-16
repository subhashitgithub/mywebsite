from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("Blog", views.Blog, name='Blog'),
    path("contact",views.contact, name='contact'),
    path("signup",views.handleSignup, name='handleSignup'),
]