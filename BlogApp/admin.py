from django.contrib import admin
from .models import Blog, Tag

class BlogAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
