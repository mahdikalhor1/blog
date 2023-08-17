from django.db import models
from django.core.validators import MinLengthValidator
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
    data = models.DateField(auto_now=True)
    title = models.CharField(max_length=50)
    excerpt = models.TextField()
    content = models.TextField(validators=[MinLengthValidator(50)])
    slug = models.SlugField(unique=True, db_index=True, default='')

    