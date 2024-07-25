from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/', UserUpdateView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password-success', password_success, name="password-success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show-profile-page"),
    path('<int:pk>/edit-profile-page/', EditProfilePageView.as_view(), name="edit-profile-page"),
]
