from django.urls import path
from . import views

urlpatterns = [
    path('', views.atividades, name='atividades'),
]