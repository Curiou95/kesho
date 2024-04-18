from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('babe/', views.babe, name='madiba'),
    path('jumper/', views.jumper, name='madiba'),
    path('about/', views.about, name='madiba'),
    path('home/', views.home, name='madiba'),
]
