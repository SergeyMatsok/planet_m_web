from django import forms
from .models import ForumPost


class ForumPostForm(forms.ModelForm):
    """Форма для создания сообщения на форуме"""
    
    class Meta:
        model = ForumPost
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите свой вопрос или ответ...',
                'rows': 4,
                'style': 'resize: vertical;'
            }),
        }
        labels = {
            'content': '',
        }