from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'keshoApp/index.html')

def home(request):
    return render(request, 'keshoApp/home.html')

def jumper(request):
    return render(request, 'keshoApp/jumper.html')

def babe(request):
    return render(request, 'keshoApp/babe.html')

def about(request):
    return render(request, 'keshoApp/about.html')



