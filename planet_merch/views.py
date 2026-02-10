from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import MerchItem, Order
from .forms import OrderForm


def merch_list(request):
    """Список всех товаров мерча"""
    # Фильтруем по статусу вместо метода is_available()
    items = MerchItem.objects.filter(
        status__in=['in_stock', 'low_stock', 'pre_order']
    ).order_by('order', '-created_at')
    
    # Фильтрация по категориям
    category = request.GET.get('category')
    if category:
        items = items.filter(category=category)
    
    # Только рекомендуемые
    featured = request.GET.get('featured')
    if featured:
        items = items.filter(is_featured=True)
    
    # Только новинки
    new_only = request.GET.get('new')
    if new_only:
        items = items.filter(is_new=True)
    
    # Статистика
    categories = MerchItem.CATEGORY_CHOICES
    featured_items = MerchItem.objects.filter(
        is_featured=True,
        status__in=['in_stock', 'low_stock', 'pre_order']
    )[:4]
    
    context = {
        'items': items,
        'categories': categories,
        'featured_items': featured_items,
        'selected_category': category,
    }
    return render(request, 'planet_merch/merch_list.html', context)



def merch_detail(request, slug):
    """Детальная страница товара"""
    item = get_object_or_404(MerchItem, slug=slug)
    
    # Похожие товары
    related_items = MerchItem.objects.filter(
        category=item.category,
        status__in=['in_stock', 'low_stock', 'pre_order']
    ).exclude(id=item.id)[:4]
    
    # Обработка формы заказа
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.merch_item = item
            order.total_price = item.price * order.quantity
            order.save()
            
            messages.success(
                request,
                f'Заказ на "{item.title}" успешно оформлен! Номер заказа: #{order.id}'
            )
            return redirect('merch_list')
    else:
        form = OrderForm()
    
    context = {
        'item': item,
        'related_items': related_items,
        'order_form': form,  # Передаём форму в шаблон
    }
    return render(request, 'planet_merch/merch_detail.html', context)


