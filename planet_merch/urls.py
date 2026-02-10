from django.urls import path
from . import views

urlpatterns = [
    path('', views.merch_list, name='merch_list'),
    path('<slug:slug>/', views.merch_detail, name='merch_detail'),
]