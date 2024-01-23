
from django.contrib import admin
from django.urls import path
from myapp.views import index, page1
from myapp import apis

urlpatterns = [
    path('profile/',apis.ProfileCreateView.as_view()),
    path('user/',apis.UserCreateAPIView.as_view()),
    path('login/',apis.LoginView.as_view()),
    path('profileupdate/<int:pk>',apis.ProfileUpdateDeleteAPIview.as_view())
]
