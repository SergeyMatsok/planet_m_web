from django.shortcuts import render
from .models import Concert
from django.utils import timezone

def tours_list(request):
    """Список концертов"""
    upcoming = Concert.objects.filter(
        status='upcoming',
        date__gte=timezone.now()
    ).order_by('date')
    
    past = Concert.objects.filter(
        status='past'
    ).order_by('-date')
    
    context = {
        'upcoming_concerts': upcoming,
        'past_concerts': past,
    }
    return render(request, 'planet_tours/tours_list.html', context)