from django.urls import path
from . import views

# URLConf- every app has own url configurations - import this to main urlconfig file
urlpatterns = [
    path('hello/', views.say_hello, name="hello"), # as playground/ is added to main urls.py file. here you only need to add hello/. Route must end with forward slash '/'. 
    path('home/', views.home, name="home"),
    path('join/', views.join, name='join'),
    path('product_entry/', views.product_entry, name='product_entry'),
    path('show_memberdb/', views.show_memberdb, name='show_memberdb'),
    path('show_productdb/', views.show_productdb, name='show_productdb'),
]