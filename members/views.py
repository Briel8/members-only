from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse

from .models import Post
from .forms import AddPostForm, SignUpForm, LogInForm

def index(request):
    posts =  Post.objects.all()
    context = {'posts': posts}

    return render(request, 'members/index.html', context)

@login_required(login_url='/login/')
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'members/detail.html', context)

@login_required(login_url='/login/')
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('members:index',)
        else:
            form = AddPostForm(request.POST)
            return render(request, 'members/add_post.html', {'form': form})
    else:
        form = AddPostForm()
    return render(request, 'members/add_post.html', {'form': form})     # I feel this line is redundancy of line 23

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log em in
            login(request, user)
            return redirect('members:index')
        return render(request, 'members/signup.html', {'form': form})
    form = SignUpForm()
    return render(request, 'members/signup.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('members:index') # Direct to the home page
        else:
            form = AuthenticationForm(data=request.POST)
        return render(request, 'members/login.html', {'form': form})
    else:
        form = LogInForm()
        return render(request, 'members/login.html', {'form': form})

def logout_member(request):
    logout(request)
    return redirect('members:index')