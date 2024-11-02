from django.urls import path, include

from forumApp.posts import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('add-book/', views.AddBookView.as_view(), name='add-book'),
    path('<int:pk>/', include([
        path('', views.DetailPageView.as_view(), name='details-book'),
        path('delete-book/', views.DeleteBookView.as_view(), name='delete-book'),
        path('edit-book/', views.EditBookView.as_view(), name='edit-book'),
    ]))
]