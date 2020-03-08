"""useitdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from useit_register import views
from useit_register.api import UserAPI

urlpatterns = [
    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('add_post', views.add_post),
    path('edit_post/<int:post_id>', views.edit_post),
    path('delete_post/<int:post_id>', views.delete_post),
    path('add_comment', views.add_comment),
    path('admin/', admin.site.urls),
    path('useit_register/1.0/', UserAPI.as_view(), name = "useit_register")
]
