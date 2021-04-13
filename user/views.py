from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def account(request):
    return HttpResponse('Hello from accounts page')

def login(request):
    return HttpResponse('Hello from login page')

def logout(request):
    return HttpResponse('Hello from logout page')

def signup(request):
    if request.method=='POST':
        email = request.POST['email']
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        is_sf = request.POST['is_sf']
        password = request.POST['pass']
        conf_password = request.POST['conf_pass']
        if len(username) < 3:
            return redirect(signup)
        if password != conf_password:
            return redirect(signup)
        new_user = authenticate(email=email, username=username, password=conf_password)
        login(request, new_user)
        
    return HttpResponse('Hello from signup page')