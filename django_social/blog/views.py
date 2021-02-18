from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

posts = [
    { 
        'author': 'PabloAceG',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'December 2, 2020'
    },
    { 
        'author': 'CoreyMS',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'December 17, 2020'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
