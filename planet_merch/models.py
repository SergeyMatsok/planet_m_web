from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


class MerchItem(models.Model):
    """Товар мерча"""
    CATEGORY_CHOICES = [
        ('clothing', 'Одежда'),
        ('accessories', 'Аксессуары'),
        ('cd', 'CD'),
        ('other', 'Другое'),
    ]
    
    STATUS_CHOICES = [
        ('in_stock', 'В наличии'),
        ('low_stock', 'Мало на складе'),
        ('out_of_stock', 'Нет в наличии'),
        ('pre_order', 'Предзаказ'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other',
        verbose_name="Категория"
    )
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена (₽)"
    )
    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Старая цена (для скидки)"
    )
    image = models.ImageField(
        upload_to='merch/',
        verbose_name="Фото товара"
    )
    additional_images = models.ManyToManyField(
        'MerchImage',
        blank=True,
        verbose_name="Дополнительные фото"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_stock',
        verbose_name="Статус"
    )
    stock_quantity = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество на складе"
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name="Рекомендуемый товар"
    )
    is_new = models.BooleanField(
        default=False,
        verbose_name="Новинка"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата добавления"
    )
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    
    def __str__(self):
        return self.title
    
    def get_discount_percent(self):
        """Возвращает процент скидки"""
        if self.old_price and self.old_price > self.price:
            return round(((self.old_price - self.price) / self.old_price) * 100)
        return 0
    
    def is_available(self):
        """Проверяет доступность товара"""
        return self.status in ['in_stock', 'low_stock', 'pre_order']


class MerchImage(models.Model):
    """Дополнительное изображение для товара"""
    image = models.ImageField(upload_to='merch/additional/')
    alt_text = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = "Дополнительное фото"
        verbose_name_plural = "Дополнительные фото"
    
    def __str__(self):
        return self.alt_text or f"Фото {self.id}"
    


class Order(models.Model):
    """Заказ"""
    STATUS_CHOICES = [
        ('pending', 'Ожидает обработки'),
        ('confirmed', 'Подтверждён'),
        ('shipped', 'Отправлен'),
        ('completed', 'Завершён'),
        ('cancelled', 'Отменён'),
    ]
    
    merch_item = models.ForeignKey(
        MerchItem,
        on_delete=models.CASCADE,
        verbose_name="Товар",
        related_name='orders'
    )
    customer_name = models.CharField(max_length=100, verbose_name="Имя")
    customer_email = models.EmailField(verbose_name="Email")
    customer_phone = models.CharField(max_length=20, verbose_name="Телефон")
    customer_address = models.TextField(verbose_name="Адрес доставки")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Итого"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Статус"
    )
    notes = models.TextField(blank=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    
    def __str__(self):
        return f"Заказ #{self.id} - {self.customer_name}"