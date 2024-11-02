from django.db import models


class LanguageChoices(models.TextChoices):
    Bulgarian = 'Bg', 'Bulgarian'
    English = 'En', 'English'
    French = 'Fr', 'French'
    German = 'Gd', 'German'
    Russian = 'Ru', 'Russian'
    Other = 'O', 'Other'
