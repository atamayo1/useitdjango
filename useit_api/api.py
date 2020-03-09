from django.shortcuts import render,redirect
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import generics
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.urls import reverse_lazy

class PostList(generics.ListCreateAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes = (IsAuthenticated,)
        authentication_class = (TokenAuthentication,)
        def post(self, request):
                serializer = PostSerializer(data = request.data)
                if serializer.is_valid():
                    post = serializer.save()
                    return Response(serializer.data, status = status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CommentList(generics.ListCreateAPIView):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer
        permission_classes = (IsAuthenticated,)
        authentication_class = (TokenAuthentication,)
        def post(self, request):
                serializer = CommentSerializer(data = request.data)
                if serializer.is_valid():
                    comment = serializer.save()
                    return Response(serializer.data, status = status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

"""class LikeList(generics.ListCreateAPIView):
        queryset = Like.objects.all()
        serializer_class = LikeSerializer
        permission_classes = (IsAuthenticated,)
        authentication_class = (TokenAuthentication,)
        def post(self, request):
                serializer = LikeSerializer(data = request.data)
                if serializer.is_valid():
                    like = serializer.save()
                    return Response(serializer.data, status = status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)"""

"""class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('useit_api:post_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)"""
