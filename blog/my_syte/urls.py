from django.urls import path
from . import views
urlpatterns = [
    path('', view= views.home_page , name = 'home-page'),
    path('posts/', view = views.posts, name= 'posts'),
    path('posts/<slug:post_name>/', view= views.post_ditails, name='post-ditails'),
    
]