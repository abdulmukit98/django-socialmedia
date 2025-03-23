# posts/model.py

from django.db import models
from django.conf import settings

class Post (models.Model):
    
    # link to user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # upload Image
    image = models.ImageField(upload_to='post_images/') 
    # optional caption
    caption = models.TextField(blank=True, null=True)
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    # A many to many like field
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)

    # Return numbers of like of a post
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user.username}'s post at {self.created_at}"


class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.post}"
    