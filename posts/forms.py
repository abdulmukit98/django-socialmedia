# posts/forms.py

from django import forms
from .models import Post, Comment


# This allow to upload an image and write captions
class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]

