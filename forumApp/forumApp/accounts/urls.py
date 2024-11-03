from django.urls import path

from forumApp.accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
]