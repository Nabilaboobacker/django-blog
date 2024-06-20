from django.contrib import admin
from . models import Blog, Comment
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'blog_slug': ('blog_title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)