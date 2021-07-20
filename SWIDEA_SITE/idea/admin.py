from django.contrib import admin
from . import models

@admin.register(models.IdeaList)
class CustomFoodAdmin(admin.ModelAdmin):
    pass
