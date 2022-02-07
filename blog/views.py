import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Blog

def index(request, **kwargs):
    blogs = Blog.objects.filter(is_published=True).order_by('-id')[0:3]
    q = request.GET.get('q')
    if q:
        blogs = Blog.objects.filter(is_published=True).filter(title__icontains=q)
    context = {'blogs': blogs, 'q': q}
    return render(request, 'index.html', context=context)

def one_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'one_post.html', context={'post': post})

def show_gallery(request):
    blogs = Blog.objects.all().order_by('-id')
    return render(request, 'gallery.html', context={'blogs':blogs})

def contacts(request):
    return render(request, 'contacts.html')