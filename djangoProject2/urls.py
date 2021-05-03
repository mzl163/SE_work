"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from miaTest import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('miaIndex', views.index),
    url(r'^register$', views.register, name='register'),
    url(r"^register_handle$", views.register_handle, name='register_handle'),
    url(r'^jumpurl$', views.jumpurl, name='jumpurl'),
    url(r'^log_on$', views.log_on, name='log_on'),
    url(r'^ad_register_handle$', views.ad_register_handle, name='ad_register_handle'),
    url(r'^customer_log_on$', views.customer_log_on, name='customer_log_on'),
    url(r'^ad_log_on$', views.ad_log_on, name='ad_log_on'),
]
