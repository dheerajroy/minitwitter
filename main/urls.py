from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CreateTweetView, IndexView, LoginView, LogoutView, ProfileView, SignupView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('createtweet', login_required(CreateTweetView.as_view()), name='createtweet'),
    path('profile', login_required(ProfileView.as_view()), name='profile')
]
