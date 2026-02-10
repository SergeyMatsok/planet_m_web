from django.contrib import admin
from .models import MerchItem, MerchImage, Order


@admin.register(MerchImage)
class MerchImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'alt_text']
    search_fields = ['alt_text']


@admin.register(MerchItem)
class MerchItemAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'price',
        'old_price',
        'status',
        'stock_quantity',
        'is_featured',
        'is_new',
        'order'
    ]
    list_editable = ['price', 'status', 'is_featured', 'is_new', 'order']
    list_filter = ['category', 'status', 'is_featured', 'is_new']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['additional_images']
    
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'slug', 'category', 'description')
        }),
        ('Цена и статус', {
            'fields': ('price', 'old_price', 'status', 'stock_quantity')
        }),
        ('Изображения', {
            'fields': ('image', 'additional_images')
        }),
        ('Дополнительно', {
            'fields': ('is_featured', 'is_new', 'order')
        }),
    )



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'merch_item',
        'customer_name',
        'customer_phone',
        'quantity',
        'total_price',
        'status',
        'created_at'
    ]
    list_editable = ['status']
    list_filter = ['status', 'created_at']
    search_fields = ['customer_name', 'customer_email', 'customer_phone']
    readonly_fields = ['created_at', 'total_price']
    
    fieldsets = (
        ('Товар', {
            'fields': ('merch_item', 'quantity', 'total_price')
        }),
        ('Клиент', {
            'fields': ('customer_name', 'customer_email', 'customer_phone', 'customer_address')
        }),
        ('Заказ', {
            'fields': ('status', 'notes', 'created_at')
        }),
    )