
from django.urls import path
from accounts import apis

urlpatterns = [
    path('profile/',apis.ProfileCreateView.as_view()),
    path('user/',apis.UserCreateAPIView.as_view()),
    path('login/',apis.LoginView.as_view()),
    path('profile/<int:pk>',apis.ProfileUpdateDeleteAPIview.as_view()),
    path('user/<int:pk>',apis.UserUpdateAPIview.as_view())
]
