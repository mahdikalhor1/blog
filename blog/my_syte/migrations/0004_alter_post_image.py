# Generated by Django 4.2.4 on 2023-08-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_syte', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(path='/my_syte/static/my_syte'),
        ),
    ]