from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'keshoApp/index.html')