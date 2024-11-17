from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from library_api.books_api.models import Book
from library_api.books_api.serializer import BookSerializer


class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    request=BookSerializer,
    responses={201: BookSerializer},
)
class BookSetView(APIView):
    @staticmethod
    def get_book(pk: int):
        return get_object_or_404(Book, pk=pk)

    @staticmethod
    def valid_serializer(serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk: int):
        book = self.get_book(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk: int):
        book = self.get_book(pk)
        serializer = BookSerializer(book, data=request.data)
        return self.valid_serializer(serializer)

    def patch(self, request, pk: int):
        book = self.get_book(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        return self.valid_serializer(serializer)

    def delete(self, request, pk: int):
        book = self.get_book(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
