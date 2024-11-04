from django.db import models

from forumApp.posts.choices import LanguageChoices
from forumApp.posts.validators import BadLanguageValidator


class Books(models.Model):
    title = models.CharField(
        max_length=30,
    )

    content = models.TextField(
        validators=[BadLanguageValidator(words=['fuck'])]
    )

    author = models.CharField(
        max_length=100
    )

    created_at = models.DateField(
        auto_now_add=True
    )

    language = models.CharField(
        max_length=30,
        choices=LanguageChoices.choices,
        default=LanguageChoices.Other
    )

    approved = models.BooleanField(
        default=False
    )

    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )

    class Meta:
        permissions = [
            ('can_approve_posts', 'Can approve posts'),
        ]


class Comments(models.Model):
    book = models.ForeignKey(
        to=Books,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=30
    )

    content = models.TextField()

    created_at = models.DateField(
        auto_now_add=True,
    )
