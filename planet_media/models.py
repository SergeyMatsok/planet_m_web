from django.db import models
from django.db import models
from django.utils import timezone


class Album(models.Model):
    """Альбом фотографий"""
    title = models.CharField(max_length=200, verbose_name="Название альбома")
    slug = models.SlugField(unique=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание")
    cover_image = models.ImageField(upload_to='albums/covers/', blank=True, null=True, verbose_name="Обложка альбома")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
    
    def __str__(self):
        return self.title
    
    def get_photo_count(self):
        """Количество фото в альбоме"""
        return self.photos.count()
    

class Photo(models.Model):
    """Фотография"""
    album = models.ForeignKey(
        Album, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='photos',
        verbose_name="Альбом"
    )
    title = models.CharField(
        max_length=200, 
        verbose_name="Название",
        blank=True  # ← ДОБАВЬТЕ ЭТУ СТРОКУ
    )
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True, verbose_name="Описание")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
    
    def __str__(self):
        return self.title or f"Фото {self.id}"


class Video(models.Model):
    """Видео (клип, промо)"""
    title = models.CharField(max_length=200, verbose_name="Название")
    youtube_url = models.URLField(verbose_name="Ссылка на YouTube")
    description = models.TextField(blank=True, verbose_name="Описание")
    thumbnail = models.ImageField(upload_to='videos/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
    
    def __str__(self):
        return self.title
    
    def get_embed_url(self):
        """Преобразует обычную ссылку в embed-ссылку для вставки"""
        if 'youtube.com/watch' in self.youtube_url:
            video_id = self.youtube_url.split('v=')[1].split('&')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        elif 'youtu.be/' in self.youtube_url:
            video_id = self.youtube_url.split('youtu.be/')[1].split('?')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        return self.youtube_url