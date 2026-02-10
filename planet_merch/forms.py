from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Форма заказа"""
    
    class Meta:
        model = Order
        fields = [
            'customer_name',
            'customer_email',
            'customer_phone',
            'customer_address',
            'quantity',
            'notes'
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            'customer_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@example.com'
            }),
            'customer_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (999) 123-45-67'
            }),
            'customer_address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите полный адрес доставки',
                'rows': 3
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'value': '1'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительные пожелания (опционально)',
                'rows': 2
            }),
        }