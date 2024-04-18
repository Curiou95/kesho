from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from . import forms

# Create your views here.

def index(request):
    return render(request, 'keshoApp/index.html')

def home(request):
    return render(request, 'keshoApp/home.html')

def jumper(request):
    return render(request, 'keshoApp/jumper.html')

def babe(request):
    return render(request, 'keshoApp/babe.html')

# trying to add a babe form
def addbabe(request):
    # addedbabe = models.Babe.objects.get(id=pk)
    babegetform = forms.AddBabeForm()
    return render(request, 'keshoApp/addbabe', {'babegetform': babegetform}) 


    babesform = forms.AddBabeForm(request.POST)
    if request.method == 'POST':
        if babesform.is_valid():
            new_babe = babesform.save(commit=False)
            new_babe.save
    return render(request, 'keshoApp/addbabe.html', {'babesform': babesform})   

def about(request):
    return render(request, 'keshoApp/about.html') 



