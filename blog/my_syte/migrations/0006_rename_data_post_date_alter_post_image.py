# Generated by Django 4.2.4 on 2023-08-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_syte', '0005_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(path='/home/mk13/code/django/blog/blog/my_syte/static/my_syte/image'),
        ),
    ]