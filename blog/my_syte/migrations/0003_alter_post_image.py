# Generated by Django 4.2.4 on 2023-08-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_syte', '0002_rename_export_post_excerpt_post_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(path='static/my_syte'),
        ),
    ]