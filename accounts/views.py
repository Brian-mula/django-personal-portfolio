from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


# Create your views here.
def login_user(request):
    return render(request,'authentication/login.html')