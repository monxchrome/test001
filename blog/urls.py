from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('updates/<int:pk>/', views.one_post, name='one_post'),
    path('updates/', views.show_gallery, name='updates'),
    path('contacts/', views.contacts, name='contacts')
]