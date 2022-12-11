from django import forms

from .models import Profile


class BlogForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['title','author','body']