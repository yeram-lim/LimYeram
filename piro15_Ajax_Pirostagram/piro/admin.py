from django.contrib import admin
from django.db import models
from . import models

# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title', 'content', 'like']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['post', 'content']
    search_fields = ('post__title', 'content')
    pass