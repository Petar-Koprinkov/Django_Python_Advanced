# Generated by Django 5.1.1 on 2024-11-03 10:35

import django.db.models.deletion
import forumApp.posts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(validators=[forumApp.posts.validators.BadLanguageValidator(words=['fuck'])])),
                ('author', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('language', models.CharField(choices=[('Bg', 'Bulgarian'), ('En', 'English'), ('Fr', 'French'), ('Gd', 'German'), ('Ru', 'Russian'), ('O', 'Other')], default='O', max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.books')),
            ],
        ),
    ]
