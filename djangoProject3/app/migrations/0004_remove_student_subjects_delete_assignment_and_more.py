# Generated by Django 5.0.4 on 2024-04-04 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_awards_award_rename_genres_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
