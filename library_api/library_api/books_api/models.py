from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=50
    )

    pages = models.IntegerField()

    description = models.TextField(
        max_length=1000,
        default=''
    )

    author = models.CharField(
        max_length=30
    )


