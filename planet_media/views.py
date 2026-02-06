from django.shortcuts import render, get_object_or_404
from .models import Photo, Video, Album
from django.shortcuts import redirect
from django.contrib import messages
from .forms import MultiplePhotoUploadForm


def gallery(request):
    """Главная страница фотогалереи — список альбомов"""
    albums = Album.objects.all()
    
    # Фото без альбома (если есть)
    orphan_photos = Photo.objects.filter(
        is_published=True,
        album__isnull=True
    ).order_by('-uploaded_at')
    
    context = {
        'albums': albums,
        'orphan_photos': orphan_photos,
    }
    return render(request, 'planet_media/gallery.html', context)


def album_detail(request, slug):
    """Страница альбома с фото"""
    album = get_object_or_404(Album, slug=slug)
    photos = album.photos.filter(is_published=True).order_by('-uploaded_at')
    
    context = {
        'album': album,
        'photos': photos,
    }
    return render(request, 'planet_media/album_detail.html', context)


def videos(request):
    """Видео"""
    videos = Video.objects.all().order_by('order')
    return render(request, 'planet_media/videos.html', {'videos': videos})


def upload_multiple_photos(request):
    """Страница массовой загрузки фото"""
    if request.method == 'POST':
        form = MultiplePhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photos = form.save()
            messages.success(request, f'Успешно загружено {len(photos)} фотографий!')
            return redirect('gallery')
    else:
        form = MultiplePhotoUploadForm()
    
    return render(request, 'planet_media/upload_multiple.html', {'form': form})