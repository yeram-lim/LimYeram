from django.contrib import admin
from django.db import models
from . import models

# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title', 'content', 'like', 'dislike']

@admin.register(models.Comment)
class CommentsAdmin(admin.ModelAdmin):
    pass