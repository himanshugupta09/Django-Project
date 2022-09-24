from django.urls import path
from . import views
  
urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),
    path('setcookie', views.setcookie),
    path('getcookie', views.showcookie),
    path('update', views.updating_cookie),
     
]