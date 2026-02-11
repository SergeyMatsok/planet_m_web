from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_index, name='forum_index'),
    path('reply/<int:post_id>/', views.add_reply, name='forum_add_reply'),
    path('like/<int:post_id>/', views.like_post, name='forum_like_post'),
]