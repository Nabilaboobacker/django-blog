from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Category crud operations
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:id>/', views.edit_categories, name='edit_categories'),
    path('categories/delete/<int:id>/', views.delete_categories, name='delete_categories'),
    # Blogs crud operations
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/add/', views.add_blog, name='add_blog'),
    path('blogs/edit/<int:id>/', views.edit_blog, name='edit_blog'),
    path('blogs/delete/<int:id>/', views.delete_blog, name='delete_blog'),
    # users
    path('users/', views.user, name='user'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:id>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:id>/', views.delete_user, name='delete_user'),
]
