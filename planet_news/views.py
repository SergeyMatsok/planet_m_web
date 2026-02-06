from django.shortcuts import render, get_object_or_404
from .models import NewsPost

def news_list(request):
    """Список новостей"""
    posts = NewsPost.objects.filter(is_published=True).order_by('-published_date')
    return render(request, 'planet_news/news_list.html', {'posts': posts})


def news_detail(request, slug):
    """Детальная страница новости"""
    post = get_object_or_404(NewsPost, slug=slug, is_published=True)
    return render(request, 'planet_news/news_detail.html', {'post': post})