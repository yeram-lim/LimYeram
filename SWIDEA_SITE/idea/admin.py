from django.contrib import admin
from . import models

@admin.register(models.IdeaList)
class CustomIdeaAdmin(admin.ModelAdmin):
    pass
