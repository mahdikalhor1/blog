from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

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

class PostDetail(View):

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        form = CommentForm()

        context = {
            'post' : post,
            'form' : form,
            'comments' : post.comments.all().order_by('-id'),
            'is_read_later' : self.is_read_later(request, slug),
        }
        

        return render(request, 'my_syte/post_detail.html', context)
    
    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse('post-details', args=[slug]))
        
       
        context = {
            'post' : post,
            'form' : form,
            'comments' : post.comments.all().order_by('-id'),
            'is_read_later' : self.is_read_later(request, slug),
        }

        return render(request, 'my_syte/post_detail.html', context)
    

    def is_read_later(self,request ,slug):
        try:
            read_later_list = request.session['read_later']
            print(slug, read_later_list)
            return slug in read_later_list
        except:
            return False

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


def read_later(request, slug):

    try:
        request.session['read_later']
    except KeyError:
        request.session['read_later'] = []

    request.session['read_later'].append(slug)

    return HttpResponseRedirect(reverse('post-details', args=[slug]))


class Read_later(TemplateView):
    template_name = 'my_syte/read_later.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        try:
            read_later_slugs = self.request.session['read_later']
            context['read_later_posts'] = []
            
            for slug in read_later_slugs:
                
                context['read_later_posts'].append(Post.objects.get(slug=slug))
        except KeyError:
            context['is_empty'] = True
        return context