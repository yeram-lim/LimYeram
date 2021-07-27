from django.db import models
from django.db.models.fields import CommaSeparatedIntegerField
from django.db.models.fields.files import ImageField

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='사진', upload_to="post_image/%Y/%m/%d/", null=True, blank=True)
    
    like = models.IntegerField(default=0, blank=True)
    dislike = models.IntegerField(default=0, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE, db_column="post_id")


