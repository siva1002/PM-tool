
from django.urls import path
from accounts import apis

urlpatterns = [
    path('profile/',apis.ProfileCreateView.as_view()),
    path('user/',apis.UserCreateAPIView.as_view(),name="user"),
    path('login/',apis.LoginView.as_view()),
    path('profile/<int:pk>',apis.ProfileUpdateDeleteAPIview.as_view()),
    path('user/<int:pk>',apis.UserUpdateAPIview.as_view()),
    path('roles',apis.RoleCreateAPIView.as_view()),
    path('role/<int:pk>',apis.RoleUpdateAPIview.as_view())
]
