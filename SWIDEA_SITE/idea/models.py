from django.db import models
from django.urls import reverse
from datetime import datetime 

# Create your models here.
class IdeaList(models.Model):
    title = models.CharField(max_length=100, help_text="아이디어명")
    image = models.ImageField(upload_to="idea_image/%Y/%m/%d/", null=True, blank=True, help_text="대표 사진")
    content = models.TextField(blank=True, help_text="아이디어 설명")
    interest = models.IntegerField(help_text="아이디어 관심도")
    dev_nodejs = "Node.js"
    dev_spring = "Spring"
    dev_django = "django"
    dev_javascript = "JavaScript"
    dev_choices = {
        (dev_nodejs, "Node.js"),
        (dev_spring, "Spring"),
        (dev_django, "django"),
        (dev_javascript , "JavaScript"),
    }
    devtool = models.CharField(choices = dev_choices, max_length=50, null=True, blank=True, help_text="예상 개발툴") 
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('idea:idea_detail', kwargs={'pk':self.pk})
