from django.contrib import admin
from .models import Concert

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'city', 'status']
    list_filter = ['status', 'city']
    search_fields = ['title', 'venue', 'city']