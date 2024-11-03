from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from forumApp.accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]