from django.contrib import admin
from .models import Item

#admin.site.register(Item) #admin사이트에 Item 저장하는 방법

@admin.register(Item) #다른 등록 방법
class ItemAdmin(admin.ModelAdmin): 
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    list_display_links = ['name']
    list_filter = ['is_publish', 'updated_at']
    search_fields = ['name']

    def short_desc(self, item):
        return item.desc[:20]
