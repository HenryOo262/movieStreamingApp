# Generated by Django 5.0.6 on 2024-07-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieStreamingApp', '0001_initial'),
        ('movie_app', '0002_remove_movie_cast_remove_movie_director_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='movie',
        ),
        migrations.AddField(
            model_name='director',
            name='movie',
            field=models.ManyToManyField(blank=True, to='movie_app.movie'),
        ),
    ]
