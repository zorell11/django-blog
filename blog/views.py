from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello Zoltan</h1>')

def posts(requests):
    return HttpResponse('<h1>Posts</h1>')