from django.shortcuts import render
from datetime import date
from .models import Post

def get_date(post):
    return post.date

def home_page(request):
    all_posts = Post.objects.all()
    latest_posts = sorted(all_posts, key=get_date)[-3:]
    return render(request, 'my_syte/home_page.html', {'posts' : latest_posts})

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'my_syte/all_posts.html', {"posts" : all_posts})

def post_ditails(request, post_name):
    post = Post.objects.get(slug=post_name)
    return render(request, 'my_syte/post_detail.html', {'post': post})