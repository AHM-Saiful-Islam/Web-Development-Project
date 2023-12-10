from django.urls import path
from berlin import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("hello/", views.hello_there, name = "hello"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
