from django.contrib import admin
from .models import Photo, Video, Album


# Inline-форма для фото внутри альбома
class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 5  # Количество пустых полей для загрузки
    fields = ['title', 'image', 'description', 'is_published']
    show_change_link = True


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_photo_count', 'created_at', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'description']
    inlines = [PhotoInline]  # ← ДОБАВЬТЕ ЭТУ СТРОКУ
    
    def get_photo_count(self, obj):
        return obj.photos.count()
    get_photo_count.short_description = 'Фото'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title_display', 'album', 'uploaded_at', 'is_published']
    list_editable = ['is_published']
    list_filter = ['album', 'is_published']
    search_fields = ['title', 'description']
    
    # Отображение "Без названия" если поле пустое
    def title_display(self, obj):
        return obj.title or "Без названия"
    title_display.short_description = "Название"
    title_display.admin_order_field = 'title'


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_platform_display', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']
    
    def get_platform_display(self, obj):
        if obj.video_file:
            return '📁 Загружено'
        elif obj.youtube_url:
            if 'youtube' in obj.youtube_url:
                return '📺 YouTube'
            elif 'vk.com' in obj.youtube_url:
                return '📺 ВКонтакте'
            else:
                return '🔗 Ссылка'
        return '—'
    get_platform_display.short_description = 'Источник'