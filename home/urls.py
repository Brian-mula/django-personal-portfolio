
from django.urls import path

from home.views import (BlogDeleteView, BlogDetailsView, BlogUpdateView,
                        BlogView, CreateBlogView, HomeView)

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('blogs',BlogView.as_view(),name='blogs'),
    path('new_blog',CreateBlogView.as_view(),name='newblog'),
    path('blogs/<int:pk>',BlogDetailsView.as_view(),name='blogdetails'),
    path('blogs/update/<int:pk>',BlogUpdateView.as_view(),name="blogupdate"),
    path("blogs/delete/<int:pk>",BlogDeleteView.as_view(),name="deleteblog")
    
]
