from django.contrib import admin
from .models import BandMember, BandInfo

@admin.register(BandMember)
class BandMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order']
    list_editable = ['order']

@admin.register(BandInfo)
class BandInfoAdmin(admin.ModelAdmin):
    list_display = ['title']