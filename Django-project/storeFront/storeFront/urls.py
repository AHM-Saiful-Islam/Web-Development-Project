"""
URL configuration for storeFront project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# add app's urls here. \for playground when req playground/hello, playground.urls app will run and run hello portion.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include("playground.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("berlin/", include("berlin.urls")),
]

urlpatterns += staticfiles_urlpatterns()
