# posts/forms.py

from django import forms
from .models import Post, Comment


# This allow to upload an image and write captions
class PostForm (forms.ModelForm):
    """
    Class for holding the forms of sending post.
    """
    class Meta:
        model = Post
        fields = ['image', 'caption']


class CommentForm(forms.ModelForm):
    """
    Class for holing the forms to write comment to a post.
    """
    class Meta:
        model = Comment
        fields = ['text',]

