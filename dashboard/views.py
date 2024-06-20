from django.shortcuts import render, redirect, get_object_or_404
from blog_app.models import Blog
from category.models import Category
from django.contrib.auth.decorators import login_required
from . forms import categoryForm, BlogPostForm, AddUserForm, EditUserForm
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login_view')
def dashboard(request):
    blog_count = Blog.objects.all().count()
    category_count = Category.objects.all().count()
    context = {
        'blog_count':blog_count,
        'category_count':category_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login_view')
def categories(request):
    return render(request, 'dashboard/categories.html')

@login_required(login_url='login_view')
def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs,}
    return render(request, 'dashboard/blogs.html', context)

def add_category(request):
    if request.method == 'POST':
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = categoryForm()
    context = {'form': form,}
    return render(request, 'dashboard/add_category.html', context)

def edit_categories(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        form = categoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = categoryForm(instance=category)
    context = {'category':category,
               'form':form,}
    return render(request, 'dashboard/edit_category.html', context)

def delete_categories(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('categories')


def add_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['blog_title']
            post.blog_slug = slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('blogs')
    else:
        form = BlogPostForm()
    context = {'form':form,}
    return render(request, 'dashboard/add_blog.html', context)



def edit_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['blog_title']
            post.blog_slug = slugify(title)
            post.save()
            return redirect('blogs')
    else:
        form = BlogPostForm(instance=blog)
    context = {'form': form,
               'blog':blog,
               }
    return render(request, 'dashboard/edit_blog.html', context)



def delete_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.delete()
    return redirect('blogs')


def user(request):
    users = User.objects.all()
    context = {'users':users, }
    return render(request, 'dashboard/user.html', context)

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
        else:
            print(form.errors)
    else:
        form = AddUserForm()
    context = {'form':form, }
    return render(request, 'dashboard/add_user.html', context)

def edit_user(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user')
        else:
            print(form.errors)
    else:
        form = EditUserForm(instance=user)
    context = {'form': form,
               'user':user,}
    return render(request, 'dashboard/edit_user.html', context)



def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    return redirect('user')