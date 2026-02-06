from django import forms
from .models import Photo, Album
from multiupload.fields import MultiFileField


class MultiplePhotoUploadForm(forms.Form):
    """Форма для загрузки нескольких фото"""
    album = forms.ModelChoiceField(
        queryset=Album.objects.all(),
        required=False,
        label="Альбом",
        help_text="Выберите альбом или оставьте пустым для загрузки без альбома"
    )
    
    images = MultiFileField(
        min_num=1,
        max_num=100,  # Максимум 100 фото за раз
        max_file_size=1024*1024*10,  # Максимум 10 МБ на файл
        label="Фотографии"
    )
    
    is_published = forms.BooleanField(
        initial=True,
        required=False,
        label="Опубликовать сразу"
    )
    
    def save(self):
        """Сохраняет все загруженные фото"""
        album = self.cleaned_data.get('album')
        is_published = self.cleaned_data.get('is_published', True)
        
        photos = []
        for image in self.cleaned_data['images']:
            title = image.name.rsplit('.', 1)[0] if image.name else ''
            
            photo = Photo.objects.create(
                album=album,
                title=title,
                image=image,
                is_published=is_published
            )
            photos.append(photo)
        
        return photos