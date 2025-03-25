from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating user profile.
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_pic', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    """
    Forms for updating user profile.
    """
    class Meta:
        model = CustomUser
        fields = ['email', 'bio', 'profile_pic']

