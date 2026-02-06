from django.db import models
from django.utils import timezone

class NewsPost(models.Model):
    """Новость или пост в блоге"""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    
    class Meta:
        ordering = ['-published_date']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    
    def __str__(self):
        return self.title