# Generated by Django 5.0.6 on 2024-08-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_movie_casts'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
