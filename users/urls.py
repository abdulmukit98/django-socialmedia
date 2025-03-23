# user/urls.py

from django.urls import path, include
from .views import register, profile, edit_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
    path('edit/', edit_profile, name='edit_profile')
]