# Generated by Django 5.1.1 on 2024-11-04 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_books_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'permissions': [('can_approve_posts', 'Can approve posts')]},
        ),
    ]
