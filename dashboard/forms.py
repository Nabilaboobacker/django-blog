from django import forms
from category.models import Category
from blog_app.models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_title', 'category', 'featured_image', 'short_description', 'description', 'is_featured', )


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions' )


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions' )
