from django.db import models


class BandMember(models.Model):
    """Участник группы"""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, verbose_name="Инструмент/роль")
    photo = models.ImageField(upload_to='members/', blank=True, null=True)
    bio = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Участник"
        verbose_name_plural = "Участники"
    
    def __str__(self):
        return self.name


class BandInfo(models.Model):
    """Общая информация о группе"""
    title = models.CharField(max_length=200, default="Название группы")
    description = models.TextField(verbose_name="Описание группы")
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    founded_year = models.IntegerField(verbose_name="Год основания")
    
    class Meta:
        verbose_name = "Информация о группе"
        verbose_name_plural = "Информация о группе"
    
    def __str__(self):
        return self.title
