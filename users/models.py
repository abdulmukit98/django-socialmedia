from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Model class for holding user profie data.

    Attributes:
        bio: Add a short description about user.
        profile_pic: users uploaded profile photo.
    
    Methods:
        __str__: Show the data in format.
    """
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


    # Display Pattern
    def __str__(self):
        """
        Display data in database in required format.

        Args:
            self: The class object itself.
        
        Returns:
            The format how it is displayed.
        """
        return self.username
    
