from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:pk>/', views.category_blog, name='category_blog'),
    path('blog/<slug:slug>/', views.single_blog, name='single_blog'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('search/', views.search, name='search'),
]
