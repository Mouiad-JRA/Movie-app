# Generated by Django 4.0.5 on 2022-06-05 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
