# users/view.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, EditProfileForm
from posts.models import Post

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the new user
            return redirect('post_list')  # Redirect to homepage after signup
    else:
        form = CustomUserCreationForm()  # ✅ Make sure the form is always defined

    return render(request, 'users/register.html', {'form': form})  # ✅ Always return an HttpResponse


def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    posts = Post.objects.filter(user=user).order_by('-created_at')
    return render(request, 'users/profile.html', {'profile_user': user, 'posts': posts})



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, 'users/edit_profile.html', {'form':form})