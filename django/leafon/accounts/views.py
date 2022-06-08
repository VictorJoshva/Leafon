from collections import UserDict
from email import message
from multiprocessing import AuthenticationError
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import auth, User
from flask import redirect

# Create your views here.
def accounts(request):
    return render(request,'accounts.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        psw=request.POST['psw']

        user = auth.authenticate(uname=uname,psw=psw)
        return redirect('/')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        # psw2=request.POST['psw2']

        user = User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)  
        print('user created')
        return redirect('/')

    else:
        return render(request, 'signup.html')

def plant(request):
    return render(request,'plant.html')



