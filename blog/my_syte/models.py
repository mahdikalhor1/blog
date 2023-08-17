from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

class Tag(models.Model):
    content = models.CharField(max_length=50)


class Post(models.Model):
    post_name = models.CharField(max_length=50)
    image = models.FilePathField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    data = models.DateField()
    title = models.CharField(max_length=50)
    export = models.TextField()
    content = models.TextField()