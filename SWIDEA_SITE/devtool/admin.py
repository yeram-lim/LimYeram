from django.contrib import admin
from . import models

@admin.register(models.Devtool)
class CustomDevtoolAdmin(admin.ModelAdmin):
    pass