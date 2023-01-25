from django import forms

from .models import Blog


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content','photo','is_published','category']