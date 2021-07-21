from functools import update_wrapper
from django.db import models

class Devtool(models.Model):
    name = models.CharField(max_length=50, help_text='>>이름')
    kind = models.CharField(max_length=50, help_text='>>종류')
    description = models.TextField(blank=True, help_text='>>개발툴 설명')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name