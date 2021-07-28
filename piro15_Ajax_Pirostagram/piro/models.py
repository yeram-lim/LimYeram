from django.db import models
from django.db.models.fields import CommaSeparatedIntegerField
from django.db.models.fields.files import ImageField

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='사진', upload_to="post_image/%Y/%m/%d/", null=True, blank=True)
    
    like = models.IntegerField(default=0, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey("Post", related_name="comment_list", on_delete=models.CASCADE, verbose_name='게시글')
    content = models.TextField(verbose_name='댓글 내용')

    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False, verbose_name='삭제여부') #댓글을 삭제할 시 ‘삭제된 댓글입니다.’ 로 표시

    def __str__(self):
        return self.content