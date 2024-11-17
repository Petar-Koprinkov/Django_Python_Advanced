from django.contrib import admin

from library_api.books_api.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

