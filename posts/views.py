from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post

# Create your views here.

@login_required
def create_post(request):
    """
    Give user access to create post to socialmeida.

    Args:
        request (HttpRequest): The incoming HTTP request.
    
    Returns:
        HttpResponse: Redirect to post_list page on successful post creation. Otherwise stays in create post form.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')     # redirecting after post
        
    else:
        form = PostForm()
    
    return render(request, 'posts/create_post.html', {'form': form})


def post_list(request):
    """
    Show a list of all post in latest creation order.

    Args:
        request: The incomming http request.
    
    Returns:
        HttpResponse: Return to post_list page.
    """
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def like_post(request, post_id):
    """
    Enable the functionality to like post.

    Args: 
        request: The incomming http request.
        post_id: The specific post which is liked.

    Returns:
        HttpResponse: Rendered Post_list template.
    """
    post = get_object_or_404(Post, id=post_id)

    # unlike if already liked
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return redirect('post_list')


@login_required
def add_comment(request, post_id):
    """
    Enable the commenting functionality. Add comment in multiple user in a specific post.

    Args:
        request: The incomming http request.
        post_id: The specific post id in which the comment is written.
    
    Returns:
        HttpResponse: Rendered to post_list template with the updated comment.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_list')
        
    else:
        form = CommentForm()
    
    return render(request, 'posts/add_comment.html', {'form': form, 'post': post})
