from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author

def get_date(post):
    return post.date

def home_page(request):
    all_posts = Post.objects.all()
    latest_posts = sorted(all_posts, key=get_date)[-3:]
    return render(request, 'my_syte/home_page.html', {'posts' : latest_posts})

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'my_syte/all_posts.html', {"posts" : all_posts})

def post_ditails(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'my_syte/post_detail.html', {'post': post})

def author(request, slug):
    authors = Author.objects.all()

    author = None
    for a in authors: 
        if a.slug() == slug:
            author = a

    return render(request, 'my_syte/author.html' ,{'author' : author})