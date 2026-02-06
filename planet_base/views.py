from django.shortcuts import render
from .models import BandInfo, BandMember
from planet_news.models import NewsPost
from planet_tours.models import Concert
from django.utils import timezone

def home(request):
    """Главная страница"""
    band_info = BandInfo.objects.first()
    members = BandMember.objects.all()
    latest_news = NewsPost.objects.filter(
        is_published=True
    ).order_by('-published_date')[:3]
    upcoming_concerts = Concert.objects.filter(
        status='upcoming',
        date__gte=timezone.now()
    ).order_by('date')[:3]
    
    context = {
        'band_info': band_info,
        'members': members,
        'latest_news': latest_news,
        'upcoming_concerts': upcoming_concerts,
    }
    return render(request, 'planet_base/home.html', context)


def about(request):
    """Страница 'О группе'"""
    band_info = BandInfo.objects.first()
    members = BandMember.objects.all()
    
    context = {
        'band_info': band_info,
        'members': members,
    }
    return render(request, 'planet_base/about.html', context)