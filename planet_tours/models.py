from django.db import models
from django.utils import timezone

class Concert(models.Model):
    """Концерт"""
    STATUS_CHOICES = [
        ('upcoming', 'Предстоящий'),
        ('past', 'Прошедший'),
        ('cancelled', 'Отменён'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название события")
    date = models.DateTimeField(verbose_name="Дата и время")
    venue = models.CharField(max_length=200, verbose_name="Место проведения")
    city = models.CharField(max_length=100, verbose_name="Город")
    address = models.CharField(max_length=300, verbose_name="Адрес")
    description = models.TextField(blank=True, verbose_name="Описание")
    ticket_url = models.URLField(blank=True, verbose_name="Ссылка на билеты")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    
    class Meta:
        ordering = ['date']
        verbose_name = "Концерт"
        verbose_name_plural = "Концерты"
    
    def __str__(self):
        return f"{self.title} - {self.date.strftime('%d.%m.%Y')}"