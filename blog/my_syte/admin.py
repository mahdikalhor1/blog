from django.contrib import admin

from .models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('post_name',),}
    list_filter = ['author', 'tag', 'date']
    list_display = ['post_name', 'author', 'date']

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)


