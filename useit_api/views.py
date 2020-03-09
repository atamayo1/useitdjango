from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from .models import Post, Comment
from .forms import PostForm, CommentForm
from rest_framework.authtoken.models import Token

def welcome(request):
    if request.user.is_authenticated:
         posts = Post.objects.all().order_by('-fix_id')
         comments = Comment.objects.all()

         return render(request, "welcome.html", {'posts': posts, 'comments': comments} )

    return redirect('/login')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')

    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    return render(request, "register.html", {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            token,_ = Token.objects.get_or_create(user = user)
            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "login.html", {'form': form})

def logout(request):
    request.user.auth_token.delete()
    do_logout(request)
    return redirect('/')

def add_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/')

    return render(request, "add_post.html", {'form': form})

def edit_post(request, post_id):
    instancia = Post.objects.get(id=post_id)

    form = PostForm(instance=instancia)

    if request.method == "POST":
        form = PostForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/')

    return render(request, "edit_post.html", {'form': form})

def delete_post(request, post_id):
    instancia = Post.objects.get(id=post_id)
    instancia.delete()

    return redirect('/')

def add_comment(request, post_id):
    form = CommentForm()
    form.fields['fix_id'].initial = post_id
    form.fields['fix_id'].widget.attrs['readonly'] = True
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/')

    return render(request, "add_comment.html", {'form': form})


