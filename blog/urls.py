from django.urls import path
from . import views


urlpatterns = [
    path('blogs/', views.index, name='index'),
    path('', views.welcome, name='index'),
    path('<int:pk>/', views.one_post, name='one_post'),
]