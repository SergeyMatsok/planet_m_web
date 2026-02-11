from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ForumPost(models.Model):
    """Сообщение на форуме (как вопрос или ответ)"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='forum_posts',
        verbose_name="Автор"
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
        verbose_name="Родительское сообщение"
    )
    content = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее обновление")
    likes = models.ManyToManyField(
        User,
        blank=True,
        related_name='liked_posts',
        verbose_name="Лайки"
    )
    
    class Meta:
        ordering = ['created_at']
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
    
    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}"
    
    def get_like_count(self):
        """Количество лайков"""
        return self.likes.count()
    
    def is_question(self):
        """Является ли сообщение вопросом (не имеет родителя)"""
        return self.parent is None
    
    def get_replies_count(self):
        """Количество ответов"""
        return self.replies.count()
    
    def get_depth(self):
        """Глубина вложенности (для отступов)"""
        depth = 0
        current = self
        while current.parent:
            depth += 1
            current = current.parent
        return depth