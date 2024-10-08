# Generated by Django 5.0.6 on 2024-08-15 11:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieStreamingApp', '0011_production'),
        ('movie_app', '0007_alter_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='productions',
            field=models.ManyToManyField(blank=True, to='movieStreamingApp.production'),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
