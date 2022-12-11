from django.contrib.auth import login
from django.shortcuts import render, redirect
from.forms import SignUpForm

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    return render(request, 'core/signup.html',)        
