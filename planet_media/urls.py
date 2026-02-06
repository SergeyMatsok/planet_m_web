from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/upload/', views.upload_multiple_photos, name='upload_multiple'),  # ← ЭТОТ МАРШРУТ ДОЛЖЕН БЫТЬ ВЫШЕ!
    path('gallery/<slug:slug>/', views.album_detail, name='album_detail'),
    path('videos/', views.videos, name='videos'),
]