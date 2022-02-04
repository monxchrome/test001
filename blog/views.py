import datetime

from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog

def index(request):
    return render(request, 'index.html',)

#def welocme_page(request):

#def get_list_blogs(request):