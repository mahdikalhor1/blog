from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def get_date(post):
    return post.date

class HomeView(TemplateView):
    template_name = 'my_syte/home_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_posts = Post.objects.all()
        latest_posts = sorted(all_posts, key=get_date)[-3:]

        context['posts'] = latest_posts
        
        return context

# def home_page(request):
#     all_posts = Post.objects.all()
#     latest_posts = sorted(all_posts, key=get_date)[-3:]
#     return render(request, 'my_syte/home_page.html', {'posts' : latest_posts})

class PostsView(ListView):
    template_name = 'my_syte/all_posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, 'my_syte/all_posts.html', {"posts" : all_posts})

class PostDetail(DetailView):
    template_name = 'my_syte/post_detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = self.get_object().comments.all()
        context['show_comments'] = True
        

        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.save()

        return HttpResponseRedirect(reverse('post-ditails', args=[kwargs['slug']]))

# def post_ditails(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'my_syte/post_detail.html', {'post': post})


class AuthorView(TemplateView):
    template_name='my_syte/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Author.objects.all()
        
        author = None
        for a in authors: 
            if a.slug() == kwargs['slug']:
                author = a

        context['author'] = author
        return context


# def author(request, slug):
#     authors = Author.objects.all()
#     author = None
#     for a in authors: 
#         if a.slug() == slug:
#             author = a

#     return render(request, 'my_syte/author.html' ,{'author' : author})

def show_comments(request):
    pass