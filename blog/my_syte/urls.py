from django.urls import path
from . import views
urlpatterns = [
    path('', view= views.HomeView.as_view() , name = 'home-page'),
    path('posts/', view = views.PostsView.as_view(), name= 'posts'),
    path('posts/<slug:slug>/read-later', view=views.read_later, name='read-later'),

    path('posts/<slug:slug>/', view= views.PostDetail.as_view(), name='post-details'),
    path('author/<slug:slug>', view= views.AuthorView.as_view() ,name='author'),
    path('read-later', view=views.Read_later.as_view(), name='read-later')
]