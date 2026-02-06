from django.contrib import admin
from .models import NewsPost

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'is_published']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}