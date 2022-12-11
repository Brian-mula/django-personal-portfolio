
from django.urls import path

from home.views import BlogView, CreateBlogView, HomeView

urlpatterns = [
    path('',HomeView.as_view()),
    path('blogs',BlogView.as_view(),name='blogs'),
    path('new_blog',CreateBlogView.as_view(),name='newblog')
    
]
