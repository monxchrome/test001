import datetime

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    created_p = "30.01.2022/13:13"
    data = datetime.datetime.now()
    res = f""" 
    <h1>Main Page</h1>
    <h2> Today date is: {data}</h2>
    <h3> Created Page: {created_p}</h3>
    """
    return HttpResponse(res)

def welocme_page(request):
    return render(request, 'index.html')