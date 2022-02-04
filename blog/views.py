import datetime

from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog

def index(request):
    blogs = Blog.objects.filter(is_published=True)
    context = {
        "blogs": blogs
    }
    return render(request, 'index.html', context=context)

def welcome(request):
    return render(request, 'welcome.html',)

def one_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    context = {
        "blogs": blogs
    }
    return render (request, 'one_post', context=context)