from django.contrib import admin

from .models import Post, Author, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('post_name',),}
    list_filter = ['author', 'tag', 'date']
    list_display = ['post_name', 'author', 'date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'post']

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)


