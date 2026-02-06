// Глобальные переменные
let currentPhotoIndex = 0;
let currentPhotoId = null;
let photos = [];

// Инициализация галереи
function initGallery(photoData) {
    photos = photoData;
    console.log('Всего фото:', photos.length);
    
    // Обработчик открытия модального окна
    document.querySelectorAll('[data-bs-toggle="modal"]').forEach(button => {
        button.addEventListener('click', function() {
            const photoId = parseInt(this.getAttribute('data-photo-id'));
            currentPhotoId = photoId;
            currentPhotoIndex = photos.findIndex(p => p.id === photoId);
            
            console.log('Открыто фото:', currentPhotoIndex + 1, 'из', photos.length);
        });
    });
    
    // Слушаем событие полного открытия модального окна
    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('shown.bs.modal', function() {
            updateModalNavigation();
        });
    });
    
    // Клавиатурная навигация
    document.addEventListener('keydown', function(e) {
        const modals = document.querySelectorAll('.modal.show');
        if (modals.length === 0) return;
        
        if (e.key === 'ArrowLeft' && currentPhotoIndex > 0) {
            currentPhotoIndex--;
            updateModalNavigation();
            e.preventDefault();
        } else if (e.key === 'ArrowRight' && currentPhotoIndex < photos.length - 1) {
            currentPhotoIndex++;
            updateModalNavigation();
            e.preventDefault();
        }
    });
}

// Функция обновления навигации
function updateModalNavigation() {
    if (!currentPhotoId) return;
    
    const modal = document.getElementById('photoModal' + currentPhotoId);
    const currentPhoto = photos[currentPhotoIndex];
    
    if (!modal) {
        console.error('Модальное окно не найдено для фото ID:', currentPhotoId);
        return;
    }
    
    // Обновляем заголовок
   // const titleEl = modal.querySelector('.modal-title');
    //if (titleEl) {
     //   titleEl.textContent = currentPhoto.title || 'Фотография ' + (currentPhotoIndex + 1);
    //}
    
    // Обновляем изображение
    const imgEl = modal.querySelector('.modal-body img');
    if (imgEl) {
        imgEl.src = currentPhoto.image;
        imgEl.alt = currentPhoto.title;
    }
    
    // Обновляем описание
    const descriptionEl = modal.querySelector('.modal-body p');
    if (descriptionEl) {
        if (currentPhoto.description) {
            descriptionEl.textContent = currentPhoto.description;
            descriptionEl.style.display = 'block';
        } else {
            descriptionEl.style.display = 'none';
        }
    }
    
    // Обновляем счётчик
    const counterEl = document.getElementById('counter' + currentPhotoId);
    if (counterEl) {
        counterEl.textContent = (currentPhotoIndex + 1) + ' из ' + photos.length;
    }
    
    // Обновляем кнопки навигации
    const prevBtn = document.getElementById('prevBtn' + currentPhotoId);
    const nextBtn = document.getElementById('nextBtn' + currentPhotoId);
    
    if (!prevBtn || !nextBtn) {
        console.error('Кнопки навигации не найдены для фото ID:', currentPhotoId);
        return;
    }
    
    if (photos.length > 1) {
        prevBtn.style.display = currentPhotoIndex > 0 ? 'inline-block' : 'none';
        nextBtn.style.display = currentPhotoIndex < photos.length - 1 ? 'inline-block' : 'none';
    } else {
        prevBtn.style.display = 'none';
        nextBtn.style.display = 'none';
    }
    
    console.log('Кнопки:', {
        prev: prevBtn.style.display,
        next: nextBtn.style.display
    });
    
    // Удаляем старые обработчики
    prevBtn.onclick = null;
    nextBtn.onclick = null;
    
    // Добавляем новые обработчики
    if (currentPhotoIndex > 0) {
        prevBtn.onclick = function() {
            currentPhotoIndex--;
            updateModalNavigation();
        };
    }
    
    if (currentPhotoIndex < photos.length - 1) {
        nextBtn.onclick = function() {
            currentPhotoIndex++;
            updateModalNavigation();
        };
    }
}

// Экспортируем функцию для использования в шаблонах
window.initGallery = initGallery;