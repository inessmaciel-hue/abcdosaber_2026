from django.urls import path
from . import views

urlpatterns = [
    path('', views.matricula, name='matricula'),
]
    