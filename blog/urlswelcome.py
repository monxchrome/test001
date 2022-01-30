from django.urls import path
from . import views

urlpatterns = [
    path('', views.welocme_page)
]