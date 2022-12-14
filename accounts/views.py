from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import CustomeUserCreationForm


# Create your views here.
def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('blogs')
        else:
            messages.success(request,("There was an error logging in"))
            return redirect('login')
    else:
        return render(request,'authentication/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    
    if request.method=="POST":
        form=CustomeUserCreationForm(request.POST or None)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('blogs')
        else:
            form=CustomeUserCreationForm()
            return render(request,'authentication/register.html') 
    else:
        return render(request,'authentication/register.html')