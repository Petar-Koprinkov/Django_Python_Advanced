# Generated by Django 5.1.1 on 2024-09-27 15:09

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
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('language', models.CharField(choices=[('Bg', 'Bulgarian'), ('En', 'English'), ('Fr', 'French'), ('Gd', 'German'), ('Ru', 'Russian'), ('O', 'Other')], default='O', max_length=30)),
            ],
        ),
    ]
