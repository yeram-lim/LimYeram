#from django.conf import settings
from django.db import models
from askcompany.utils import uuid_upload_to

class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODE, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)#on_delete=models.CASCADE: 소속된 post가 삭제되면 comment도 삭제된다.
    message = models.TextField()