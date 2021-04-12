from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def account(request):
    return HttpResponse('Hello from accounts page')

def login(request):
    return HttpResponse('Hello from login page')

def logout(request):
    return HttpResponse('Hello from logout page')

def signup(request):
    return HttpResponse('Hello from signup page')