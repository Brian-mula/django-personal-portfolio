from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from home.models import Profile

from .forms import BlogForm, UpdateBlogForm


# Create your views here.
class HomeView(ListView):
    model=Profile
    template_name='index.html'


class BlogView(ListView):
    model=Profile
    template_name='blogs.html'

    def get_queryset(self,*args,**kwargs):
        qs=super().get_queryset(*args,**kwargs)
        qs=qs.order_by("-id")
        return qs
    

class CreateBlogView(CreateView):
    model=Profile
    template_name='new_blog.html'
    form_class=BlogForm

    def get_success_url(self):
        return reverse_lazy('blogs')

    
    
class BlogDetailsView(DetailView):
    queryset=Profile.objects.all()
    template_name='blog_details.html'

class BlogUpdateView(UpdateView):
    model=Profile
    form_class=UpdateBlogForm
    template_name="blog_update.html"
    
    def get_success_url(self):
        return reverse_lazy('blogs')

    
    
class BlogDeleteView(DeleteView):
    model=Profile
    template_name="delete_blog.html"
    
    def get_success_url(self):
        return reverse_lazy('blogs')
    
   