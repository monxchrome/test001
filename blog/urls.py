from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.index),
    path('welcome/', views.welocme_page),
    path('adminsite/adminall/', views.get_list_blogs),
]