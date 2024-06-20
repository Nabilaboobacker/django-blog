from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from . models import Blog, Comment
from category . models import Category
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.db.models import Q


# Create your views here.


def home(request):
    featured_post = Blog.objects.filter(is_featured=True)
    recent_posts = Blog.objects.filter(is_featured=False).order_by('created_at')
    context = {'featured_post':featured_post,
               'recent_posts':recent_posts }
    return render(request, 'home.html', context)


def category_blog(request, pk):
    category_blogs = Blog.objects.filter(category=pk)
    category = get_object_or_404(Category, pk=pk)
    context = {'category_blogs':category_blogs,
               'category':category,
               }
    return render(request, 'category_blog.html', context)

def single_blog(request, slug):
    blog = get_object_or_404(Blog, blog_slug=slug)    
    comments = Comment.objects.filter(blog=blog)
    comment_count = comments.count()
    if request.method == 'POST':
        comment_text = request.POST['comment']
        if comment_text:
            comment = Comment.objects.create(comment=comment_text, user=request.user, blog=blog)
            comment.save()
            return HttpResponseRedirect(request.path)

    context = {
        'blog':blog,
        'comments':comments,
        'comment_count':comment_count,
    }
    return render(request, 'single_blog.html', context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email exists")
                return redirect('register')

            else:
                hashed_password = make_password(password)
                user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=hashed_password)
                user.save()
                return redirect('login_view')
        else:
            messages.error(request, 'password error')
            return redirect('register')
        
    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'login error')
            return redirect('login_view')
    return render(request, 'login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('home')

def search(request):
    search_keyword = request.GET['search_keyword']
    blogs = Blog.objects.filter(Q(blog_title__icontains=search_keyword) | Q(description__icontains=search_keyword))
    context = {'blogs':blogs,
               'search_keyword':search_keyword,}
    return render(request, 'search.html', context)