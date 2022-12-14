from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


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
    form=UserCreationForm(request.POST or None)
    if request.method=="POST":
        
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            pasword=form.cleaned_data['password']
            user=authenticate(request,username=username,pasword=pasword)
            login(request,user)
            return redirect('blogs')
        else:
            form=UserCreationForm()
            return 
    else:
        return render(request,'authentication/register.html',{'form':form})