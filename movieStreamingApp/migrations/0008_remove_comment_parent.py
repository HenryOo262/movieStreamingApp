# Generated by Django 5.0.6 on 2024-08-10 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieStreamingApp', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
