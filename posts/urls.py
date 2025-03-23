# posts/urls.py

from django.urls import path
from .views import create_post, post_list, like_post, add_comment

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('', post_list, name='post_list'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('comment/<int:post_id>/', add_comment, name='add_comment'),
]