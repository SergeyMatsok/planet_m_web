from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import ForumPost
from .forms import ForumPostForm


def forum_index(request):
    """Главная страница форума - все вопросы"""
    # Получаем только вопросы (сообщения без родителя)
    questions = ForumPost.objects.filter(parent__isnull=True).select_related('author').prefetch_related('replies')
    
    # Пагинация (10 вопросов на страницу)
    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Форма для нового вопроса
    if request.method == 'POST' and request.user.is_authenticated:
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Ваш вопрос опубликован!')
            return redirect('forum_index')
    else:
        form = ForumPostForm()
    
    context = {
        'page_obj': page_obj,
        'form': form,
    }
    return render(request, 'planet_forum/index.html', context)


@login_required
def add_reply(request, post_id):
    """Добавить ответ к вопросу или комментарию"""
    parent_post = get_object_or_404(ForumPost, id=post_id)
    
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent = parent_post
            reply.save()
            messages.success(request, 'Ответ добавлен!')
            return redirect('forum_index')
    
    return redirect('forum_index')


@login_required
def like_post(request, post_id):
    """Поставить/убрать лайк"""
    post = get_object_or_404(ForumPost, id=post_id)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return redirect('forum_index')