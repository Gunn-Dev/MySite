from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogpost, name='blog_post_list'),
    path('<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
]
