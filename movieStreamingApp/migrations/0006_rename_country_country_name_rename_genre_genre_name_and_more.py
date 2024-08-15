# Generated by Django 5.0.6 on 2024-08-05 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieStreamingApp', '0005_rename_movie_country_movies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='country',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='movies',
        ),
    ]
