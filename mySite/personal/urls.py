from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('index/', views.index, name='index'),
]