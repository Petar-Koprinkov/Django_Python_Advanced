from django.urls import path

from library_api.books_api import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
]