# Generated by Django 5.0.6 on 2024-06-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_slug',
            field=models.SlugField(default='', max_length=250, unique=True),
        ),
    ]