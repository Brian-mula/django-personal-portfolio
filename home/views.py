from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from home.models import Profile

from .forms import BlogForm


# Create your views here.
class HomeView(ListView):
    model=Profile
    template_name='index.html'


class BlogView(View):
    model=Profile
    template_name='blogs.html'
    def getblogs(self,request):
        blogs=Profile.objects.all()
        print(f"got blogs {blogs}")

        if request.method=='POST':
            form=BlogForm(request.form)
            if form.is_valid():
                form.save()

        else:
            form=BlogForm()
        return render(request,'blogs.html',{'blogs':blogs})
  
    
    
    
   