from django.urls import path
from . import views

urlpatterns = [
    path('', views.tours_list, name='tours_list'),
]