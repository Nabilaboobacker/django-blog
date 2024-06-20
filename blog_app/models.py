from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.


class Blog(models.Model):
    blog_title = models.CharField(max_length=200, unique=True)
    blog_slug = models.SlugField(max_length=250, unique=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='images/blog/')
    short_description = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.blog_title
    

class Comment(models.Model):
    comment = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment