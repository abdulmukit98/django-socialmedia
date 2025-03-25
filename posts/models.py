# posts/model.py

from django.db import models
from django.conf import settings

class Post (models.Model):
    """
    The class for each post in the homepage.

    Attributes:
        user: Foreign Key from users table. Hold the username of a post.
        image: Photo uploaded for a post.
        caption: Details of the post and image caption.
        created_at: show post in newest first.
        likse: Users like for post.

    Methods:
        total_likes: show number of total likes in a post.
        __str__: display post data in database format.
    """
    
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
        """
        Show number of likes of a post.
        """
        return self.likes.count()

    def __str__(self):
        return f"{self.user.username}'s post at {self.created_at}"


class Comment (models.Model):
    """
    Database model for adding comment to a post.

    Attributes:
        post: link to the post in which the comment is.
        user: The user who write the comment.
        text: comment body.
        created_at: timestamp
        
    Methods:
        __str__: display in database.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.post}"
    