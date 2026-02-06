from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('planet_base.urls')),
    path('news/', include('planet_news.urls')),
    path('tours/', include('planet_tours.urls')),
    path('media/', include('planet_media.urls')),
]

# Для отладки — раздача медиафайлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)