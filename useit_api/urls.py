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
from django.urls import path
from useit_api import views
from useit_api.api import UserAPI, PostList, CommentList

urlpatterns = [
    path('api/users', UserAPI.as_view(), name="users"),
    path('api/post_list', PostList.as_view(), name = 'post_list'),
    path('api/comment_list', CommentList.as_view(), name = 'comment_list'),
    #path('api/like_list', LikeList.as_view(), name = 'like_list'),
    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('add_post', views.add_post),
    path('edit_post/<int:post_id>', views.edit_post),
    path('delete_post/<int:post_id>', views.delete_post),
    path('add_comment/<int:post_id>', views.add_comment),
]
