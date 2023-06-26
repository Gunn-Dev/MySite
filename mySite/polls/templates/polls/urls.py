from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # Other URL patterns
    path('register/', views.register, name='register'),
]