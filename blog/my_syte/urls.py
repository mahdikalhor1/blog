from django.urls import path
from . import views
urlpatterns = [
    path('', view= views.HomeView.as_view() , name = 'home-page'),
    path('posts/', view = views.PostsView.as_view(), name= 'posts'),
    path('posts/<slug:slug>/', view= views.PostDetail.as_view(), name='post-ditails'),
    path('author/<slug:slug>', view= views.AuthorView.as_view() ,name='author')
]