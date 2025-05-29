from django.urls import path
from .views import index, posts

urlpatterns = [
    path('', index, name='index'),
    path('posts/', posts, name='posts')
]