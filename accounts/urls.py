
from django.urls import path
from accounts import apis
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/',apis.ProfileCreateView.as_view()),
    path('user/',apis.UserCreateAPIView.as_view(),name="user"),
    path('login/',apis.LoginView.as_view()),
    path('profile/<int:pk>',apis.ProfileUpdateDeleteAPIview.as_view()),
    path('user/<int:pk>',apis.UserUpdateAPIview.as_view()),
    path('roles',apis.RoleCreateAPIView.as_view()),
    path('role/<int:pk>',apis.RoleUpdateAPIview.as_view()),

    #---------------------#
    # Password Reset URLS #
    #---------------------#
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-reset/', views.ResetPasswordResetView.as_view(), name='password_reset'),

    
]
