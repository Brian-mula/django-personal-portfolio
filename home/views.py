from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView

from home.models import Profile

from .forms import BlogForm


# Create your views here.
class HomeView(ListView):
    model=Profile
    template_name='index.html'


class BlogView(ListView):
    model=Profile
    template_name='blogs.html'
    

class CreateBlogView(CreateView):
    model=Profile
    template_name='new_blog.html'
    form_class=BlogForm
    
    
    
   