from django.urls import path
from . import views

# URLConf- every app has own url configurations - import this to main urlconfig file
urlpatterns = [
    path('hello/', views.say_hello, name="hello"), # as playground/ is added to main urls.py file. here you only need to add hello/. Route must end with forward slash '/'. 
    path("home/", views.home, name="home"),
]