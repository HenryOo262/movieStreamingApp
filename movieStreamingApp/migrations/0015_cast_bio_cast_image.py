# Generated by Django 5.0.6 on 2024-08-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieStreamingApp', '0014_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cast',
            name='image',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
