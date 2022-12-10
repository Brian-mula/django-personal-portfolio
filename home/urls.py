
from django.urls import path

from home.views import BlogView, HomeView

urlpatterns = [
    path('',HomeView.as_view()),
    path('blogs',BlogView.as_view(),name='blogs'),
    
]
