from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.

def posts(requests):
    posts = Post.objects.all()
    print(posts)
    return render(requests, 'blog/index.html', {'posts': posts})


def post_detail(requests, id):
    post = Post.objects.get(id=id)
    return render(requests, 'blog/post_detail.html', {'post': post})