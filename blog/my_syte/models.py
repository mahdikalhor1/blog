from django.db import models
from django.core.validators import MinLengthValidator
from blog.settings import BASE_DIR
import os 
from django.utils.text import slugify
from django.urls import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)


    def name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.name()
    
    def slug(self):
        return slugify(self.name())
    
    def get_absolute_url(self):
        return reverse('author', kwargs={'slug' : self.slug()})
    

class Tag(models.Model):
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content

class Post(models.Model):
    post_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=50)
    excerpt = models.TextField()
    content = models.TextField(validators=[MinLengthValidator(50)])
    slug = models.SlugField(unique=True, db_index=True, default='')


    def __str__(self):
        return self.post_name


class Comment(models.Model):
    username = models.CharField(max_length=100)
    post = models.ForeignKey(Post, db_index=True, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.username}\n{self.content}'